#! /usr/bin/python3 
########################################################################################################################
## Copyright 2021 Datum Technology Corporation
########################################################################################################################
## SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
## Licensed under the Solderpad Hardware License v 2.1 (the "License"); you may not use this file except in compliance
## with the License, or, at your option, the Apache License version 2.0.  You may obtain a copy of the License at
##                                        https://solderpad.org/licenses/SHL-2.1/
## Unless required by applicable law or agreed to in writing, any work distributed under the License is distributed on
## an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the License for the
## specific language governing permissions and limitations under the License.
########################################################################################################################


import os
from datetime import datetime
import mio
import yaml
from yaml.loader import SafeLoader


def add_sim_to_history_log(snapshot, test_name, seed, args, results_path):
    now = datetime.now()
    timestamp = now.strftime("%Y/%m/%d-%H:%M:%S")
    
    if not os.path.exists(mio.history_file_path):
        f = open(mio.history_file_path, "w+")
        f.write("---")
        f.close()
    with open(mio.history_file_path,'r') as yamlfile:
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
            cur_yaml[snapshot]['simulations'][results_path]['cov'] = mio.sim_cov
            cur_yaml[snapshot]['simulations'][results_path]['waves'] = mio.sim_waves
            with open(mio.history_file_path,'w') as yamlfile:
                yaml.dump(cur_yaml, yamlfile) # Also note the safe_dump




def update_sim_timestamp_in_history_log(snapshot, orig_timestamp, tests_results_path):
    now = datetime.now()
    duration = now - orig_timestamp
    timestamp = now.strftime("%Y/%m/%d-%H:%M:%S")
    if not os.path.exists(mio.history_file_path):
        print("No history log file!")
    with open(mio.history_file_path,'r') as yamlfile:
        cur_yaml = yaml.load(yamlfile, Loader=SafeLoader) # Note the safe_load
        if not cur_yaml:
            print("Failed to open history log file")
            return
        else:
            cur_yaml[snapshot]['simulations'][tests_results_path]['end'] = timestamp
            cur_yaml[snapshot]['simulations'][tests_results_path]['duration'] = duration.seconds
            with open(mio.history_file_path,'w') as yamlfile:
                yaml.dump(cur_yaml, yamlfile) # Also note the safe_dump




def sim(cfg, ip_name, test, seed, verbosity, args):
    with open(mio.dv_path + "/" + ip_name + "/ip.yml", 'r') as yamlfile:
        dv_yaml = yaml.load(yamlfile, Loader=SafeLoader)
        if dv_yaml:
            test_name = dv_yaml['hdl-src']['test-name-template'].replace("{{ name }}", test)
            do_sim(cfg, ip_name, test_name, seed, verbosity, args)




def do_sim(cfg, lib_name, name, seed, verbosity, plus_args):
    
    snapshot = lib_name + "_tb"
    test_name = name
    waves_str = ""
    gui_str   = ""
    runall_str   = ""
    
    tests_results_path = mio.pwd + "/results/" + test_name + "_" + str(seed)
    
    orig_plus_args = list(plus_args)
    plus_args.append("SIM_DIR_RESULTS="                 + mio.pwd + "/results")
    plus_args.append("UVM_TESTNAME="                    + test_name)
    plus_args.append("UVML_FILE_BASE_DIR_SIM="          + mio.pwd)
    plus_args.append("UVML_FILE_BASE_DIR_TB="           + mio.dv_path  + "/" + lib_name + "/src")
    plus_args.append("UVML_FILE_BASE_DIR_TESTS="        + mio.dv_path  + "/" + lib_name + "/src/tests")
    plus_args.append("UVML_FILE_BASE_DIR_TEST_RESULTS=" + tests_results_path)
    plus_args.append("UVML_FILE_BASE_DIR_DV="           + mio.dv_path)
    plus_args.append("UVML_FILE_BASE_DIR_RTL="          + mio.rtl_path)
    
    if (verbosity != None):
        plus_args.append("UVM_VERBOSITY=UVM_" + verbosity.upper())

    act_args = ""
    for arg in plus_args:
        act_args = act_args + " -testplusarg \"" + arg + "\""
    
    if not os.path.exists(tests_results_path):
        os.mkdir(tests_results_path)
    if not os.path.exists(tests_results_path + "/trn_log"):
        os.mkdir(tests_results_path + "/trn_log")
    
    if (mio.dbg == True):
        print("Call to do_sim(snapshot='" + snapshot + "', test_name='" + test_name + "', seed='" + str(seed) + "', args='" + act_args + "')")
    
    print("\033[0;32m**********")
    print("Simulating")
    print("**********\033[0m")
    
    if (cfg['sim_waves'] == True):
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
    
    if (cfg['sim_cov'] == True):
        cov_str = ""
    else: 
        cov_str = ""
    
    if (cfg['sim_gui'] == True):
        gui_str = " --gui "
        runall_str = ""
        waves_str = ""
    else:
        gui_str = ""
        if (cfg['sim_waves'] == True):
            runall_str = ""
        else:
            runall_str = " --runall --onerror quit"
    
    if (cfg['sim_cov'] == True):
        #cov_str = " -cov_db_name " + name + "_" + str(seed) + " -cov_db_dir " + tests_results_path + "/cov"
        cov_str = ""
    else: 
        cov_str = " -ignore_coverage "
    
    add_sim_to_history_log(lib_name, name, seed, orig_plus_args, tests_results_path)
    now = datetime.now()
    mio.run_xsim_bin("xsim", snapshot + gui_str + waves_str + cov_str + runall_str + " " + act_args + " --stats --log " + tests_results_path + "/sim.log")
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
    if (cfg['sim_waves'] == True):
        print("View waves: " + mio.vivado_path + "xsim -gui ./results/" + test_name + "_" + str(seed) + "/waves.wdb &")
    print("************************************************************************************************************************")
