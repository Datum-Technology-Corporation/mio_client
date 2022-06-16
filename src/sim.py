# Copyright Datum Technology Corporation
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
########################################################################################################################


import cfg
import clean
import cmp
import cov
import dox
import elab
import history
import results
import vivado

import os
from datetime import datetime
import yaml
from yaml.loader import SafeLoader


def add_sim_to_history_log(snapshot, test_name, seed, args, results_path):
    now = datetime.now()
    timestamp = now.strftime("%Y/%m/%d-%H:%M:%S")
    
    if not os.path.exists(cfg.history_file_path):
        f = open(cfg.history_file_path, "w+")
        f.write("---")
        f.close()
    with open(cfg.history_file_path,'r') as yamlfile:
        cur_yaml = yaml.load(yamlfile, Loader=SafeLoader) # Note the safe_load
        if not cur_yaml:
            print("Failed to open history log file")
            return
        else:
            if not snapshot in cur_yaml:
                cur_yaml[snapshot] = {}
            if not 'simulations' in cur_yaml[snapshot]:
                cur_yaml[snapshot]['simulations'] = {}
            cur_yaml[snapshot]['simulations'][results_path] = {}
            cur_yaml[snapshot]['simulations'][results_path]['test_name'] = test_name
            cur_yaml[snapshot]['simulations'][results_path]['seed'] = seed
            cur_yaml[snapshot]['simulations'][results_path]['args'] = args
            cur_yaml[snapshot]['simulations'][results_path]['results'] = results_path
            cur_yaml[snapshot]['simulations'][results_path]['start'] = timestamp
            cur_yaml[snapshot]['simulations'][results_path]['cov'] = cfg.sim_cov
            cur_yaml[snapshot]['simulations'][results_path]['waves'] = cfg.sim_waves
            with open(cfg.history_file_path,'w') as yamlfile:
                yaml.dump(cur_yaml, yamlfile) # Also note the safe_dump




def update_sim_timestamp_in_history_log(snapshot, orig_timestamp, tests_results_path):
    now = datetime.now()
    duration = now - orig_timestamp
    timestamp = now.strftime("%Y/%m/%d-%H:%M:%S")
    if not os.path.exists(cfg.history_file_path):
        print("No history log file!")
    with open(cfg.history_file_path) as yamlfile:
        cur_yaml = yaml.load(yamlfile, Loader=SafeLoader) # Note the safe_load
        if not cur_yaml:
            print("Failed to open history log file")
            return
        else:
            cur_yaml[snapshot]['simulations'][tests_results_path]['end'] = timestamp
            cur_yaml[snapshot]['simulations'][tests_results_path]['duration'] = duration.seconds
            with open(cfg.history_file_path,'w') as yamlfile:
                yaml.dump(cur_yaml, yamlfile) # Also note the safe_dump




def sim(ip_name, test, seed, verbosity, args):
    with open(cfg.dv_path + "/" + ip_name + "/ip.yml", 'r') as yamlfile:
        dv_yaml = yaml.load(yamlfile, Loader=SafeLoader)
        if dv_yaml:
            test_name = dv_yaml['hdl-src']['test-name-template'].replace("{{ name }}", test)
            do_sim(ip_name, test_name, seed, verbosity, args)




def do_sim(lib_name, name, seed, verbosity, plus_args):
    
    snapshot = lib_name + "_tb"
    test_name = name
    waves_str = ""
    gui_str   = ""
    runall_str   = ""
    
    tests_results_path = cfg.pwd + "/results/" + test_name + "_" + str(seed)
    
    orig_plus_args = list(plus_args)
    plus_args.append("SIM_DIR_RESULTS="                 + cfg.pwd + "/results")
    plus_args.append("UVM_TESTNAME="                    + test_name)
    plus_args.append("UVML_FILE_BASE_DIR_SIM="          + cfg.pwd)
    plus_args.append("UVML_FILE_BASE_DIR_TB="           + cfg.dv_path  + "/" + lib_name + "/src")
    plus_args.append("UVML_FILE_BASE_DIR_TESTS="        + cfg.dv_path  + "/" + lib_name + "/src/tests")
    plus_args.append("UVML_FILE_BASE_DIR_TEST_RESULTS=" + tests_results_path)
    plus_args.append("UVML_FILE_BASE_DIR_DV="           + cfg.dv_path)
    plus_args.append("UVML_FILE_BASE_DIR_RTL="          + cfg.rtl_path)
    
    if (verbosity != None):
        plus_args.append("UVM_VERBOSITY=UVM_" + verbosity.upper())

    act_args = ""
    for arg in plus_args:
        act_args = act_args + " -testplusarg \"" + arg + "\""
    
    if not os.path.exists(tests_results_path):
        os.mkdir(tests_results_path)
    if not os.path.exists(tests_results_path + "/trn_log"):
        os.mkdir(tests_results_path + "/trn_log")
    
    if (cfg.dbg == True):
        print("Call to do_sim(snapshot='" + snapshot + "', test_name='" + test_name + "', seed='" + str(seed) + "', args='" + act_args + "')")
    
    print("\033[0;32m**********")
    print("Simulating")
    print("**********\033[0m")
    
    if (cfg.glb_cfg['sim_waves'] == True):
        if not os.path.exists(tests_results_path + "/run.xsim.tcl"):
            f = open(tests_results_path + "/run.xsim.tcl", "w")
            f.write("log_wave -recursive *")
            f.write("\n")
            f.write("run -all")
            f.write("\n")
            f.write("quit")
            f.close()
        waves_str = " --wdb " + tests_results_path + "/waves.wdb --tclbatch " + tests_results_path + "/run.xsim.tcl"
    else:
        waves_str = ""
    
    if (cfg.glb_cfg['sim_gui'] == True):
        gui_str = " --gui "
        runall_str = ""
        waves_str = ""
    else:
        gui_str = ""
        if (cfg.glb_cfg['sim_waves'] == True):
            runall_str = ""
        else:
            runall_str = " --runall --onerror quit"
    
    if (cfg.glb_cfg['sim_cov'] == True):
        if not os.path.exists(tests_results_path + "/cov"):
            os.mkdir(tests_results_path + "/cov")
        cov_str = " -cov_db_name " + name + "_" + str(seed) + " -cov_db_dir " + tests_results_path + "/cov"
    else: 
        cov_str = " -ignore_coverage "
    
    add_sim_to_history_log(lib_name, name, seed, orig_plus_args, tests_results_path)
    now = datetime.now()
    vivado.run_bin("xsim", snapshot + gui_str + waves_str + cov_str + runall_str + " " + act_args + " --stats --log " + tests_results_path + "/sim.log")
    update_sim_timestamp_in_history_log(lib_name, now, tests_results_path)
    print("************************************************************************************************************************")
    print("* View compilation/elaboration results")
    print("************************************************************************************************************************")
    print("Compilation: emacs ./results/" + lib_name + ".cmp.log &")
    print("Elaboration: emacs ./results/" + lib_name + ".elab.log &")
    print("************************************************************************************************************************")
    print("* View simulation results")
    print("************************************************************************************************************************")
    print("Open log file: emacs ./results/" + test_name + "_" + str(seed) + "/sim.log &")
    if (cfg.sim_waves == True):
        print("View waves: " + cfg.vivado_path + "xsim -gui ./results/" + test_name + "_" + str(seed) + "/waves.wdb &")
    print("************************************************************************************************************************")
