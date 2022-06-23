# Copyright Datum Technology Corporation
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
########################################################################################################################


import cfg
import clean
import cmp
import cov
import dox
import history
import results
import sim
import vivado
import discovery
import utilities

import re
import yaml
from yaml.loader import SafeLoader
from datetime import datetime
#import mio
import os


def add_elab_to_history_log(snapshot, elaboration_log_path):
    now = datetime.now()
    timestamp = now.strftime("%Y/%m/%d-%H:%M:%S")
    utilities.create_history_log()
    with open(cfg.history_file_path,'r') as yamlfile:
        cur_yaml = yaml.load(yamlfile, Loader=SafeLoader) # Note the safe_load
        if not snapshot in cur_yaml:
            cur_yaml[snapshot] = {}
        cur_yaml[snapshot]['elaboration_timestamp'] = timestamp
        cur_yaml[snapshot]['elaboration_log_path' ] = elaboration_log_path
    if cur_yaml:
        with open(cfg.history_file_path,'w') as yamlfile:
            yaml.dump(cur_yaml, yamlfile) # Also note the safe_dump




def elab(ip_name, args):
    if ip_name not in discovery.ip_paths:
        sys.exit("Failed to find IP '" + ip_name + "'.  Exiting.")
    else:
        ip_path     = discovery.ip_paths   [ip_name]
        ip_metadata = discovery.ip_metadata[ip_name]
    
    if 'dut' in ip_metadata:
        rtl_ip_name = ip_metadata['dut']['name']
        rtl_ip_type = ip_metadata['dut']['ip-type']
        top_dv_constructs = ip_metadata['hdl-src']['top-constructs']
        
        if (rtl_ip_type == "mio"):
            if rtl_ip_name not in discovery.ip_paths:
                sys.exit("Failed to find RTL IP '" + rtl_ip_name + "'.  Exiting.")
            else:
                rtl_ip_path     = discovery.ip_paths   [rtl_ip_name]
                rtl_ip_metadata = discovery.ip_metadata[rtl_ip_name]
            
            rtl_sub_type = rtl_ip_metadata['ip']['sub-type'].lower().strip()
            if (rtl_sub_type == "vivado"):
                rtl_lib_name = rtl_ip_metadata['hdl-src']['lib-name']
                xilinx_libs  = rtl_ip_metadata['hdl-src']['xilinx-libs']
                top_rtl_constructs = rtl_ip_metadata['hdl-src']['top-constructs']
                do_dut_vivado_elab(ip_name, rtl_lib_name, xilinx_libs, top_dv_constructs, top_rtl_constructs, args)
            else:
                print("ERROR: Elaboration of non-Vivado RTL Project DUTs is not yet supported")
        elif (rtl_ip_type == "fsoc"):
            fsoc_fname  = ip_metadata['dut']['full-name']
            file_path_partial_name = re.sub(r':', '_', fsoc_fname)
            eda_file_dir = cfg.pwd + "/fsoc/" + rtl_ip_name + "/sim-xsim"
            eda_file_path = eda_file_dir + "/" + file_path_partial_name + "_0.eda.yml"
            
            if os.path.exists(eda_file_path):
                with open(eda_file_path, 'r') as edafile:
                    eda_yaml = yaml.load(edafile, Loader=SafeLoader)
                    if eda_yaml:
                        elab_options = eda_yaml['tool_options']['xsim']['xelab_options']
                        do_dut_fsoc_elab(ip_name, rtl_ip_name, top_dv_constructs, args)
                    else:
                        print("ERROR: Unable to parse " + edafile)
            else:
                print("ERROR: Could not find " + edafile)
        else:
            return
    else:
        top_hdl_unit = ip_metadata['hdl-src']['top-constructs']
        do_elab(ip_name, top_hdl_unit, args)




def do_dut_vivado_elab(ip_name, lib_name, xilinx_libs, top_dv_constructs, top_rtl_constructs, args):
    print("\033[0;36m***********")
    print("Elaborating")
    print("***********\033[0m")
    elaboration_log_path = cfg.sim_results_dir + "/" + lib_name + ".elab.log"
    lib_string = ""
    top_rtl_constructs_string = ""
    top_dv_constructs_string = ""
    for construct in top_rtl_constructs:
        top_rtl_constructs_string = top_rtl_constructs_string + " " + construct
    for construct in top_dv_constructs:
        top_dv_constructs_string = top_dv_constructs_string + " " + ip_name + "." + construct
    for lib in xilinx_libs:
        lib_string = lib_string + " -L " + lib
    vivado.run_bin("xelab", " --relax " + args + " -debug all --mt auto -L " + ip_name + "=./out/" + ip_name + " -L " + lib_name + lib_string + " --snapshot " + top_dv_constructs[0] + " " + top_dv_constructs_string + " " + top_rtl_constructs_string + " --log " + elaboration_log_path)
    add_elab_to_history_log(ip_name, elaboration_log_path)
    




def do_dut_fsoc_elab(ip_name, lib_name, top_dv_constructs, args):
    top_dv_constructs_string = ""
    for construct in top_dv_constructs:
        top_dv_constructs_string = top_dv_constructs_string + " " + lib_name + "." + construct
    print("\033[0;36m***********")
    print("Elaborating")
    print("***********\033[0m")
    elaboration_log_path = cfg.pwd + "/results/" + lib_name + ".elab.log"
    vivado.run_bin("xelab", " --incr -dup_entity_as_module -relax " + args + " --O0 -v 0 -timescale 1ns/1ps -L " + ip_name + "=./out/" + ip_name + " -L " + lib_name + "=./out/" + lib_name + " --snapshot " + top_dv_constructs[0] + " " + top_dv_constructs_string + " --log " + elaboration_log_path)
    add_elab_to_history_log(ip_name, elaboration_log_path)
    




def do_elab(lib_name, top_dv_constructs, args):
    
    debug_str = ""
    top_dv_constructs_string = ""

    if (cfg.dbg):
        print("Call to do_elab(lib_name='" + lib_name + "', design_unit='" + top_dv_constructs[0] + "')")
    print("\033[0;36m***********")
    print("Elaborating")
    print("***********\033[0m")
    
    for construct in top_dv_constructs:
        top_dv_constructs_string = top_dv_constructs_string + " " + lib_name + "." + construct
    
    if (cfg.sim_debug):
        debug_str = " --debug all "
    else:
        debug_str = " --debug typical "
    
    if (cfg.glb_cfg['sim_cov'] == True):
        # TODO Move this to sim, not elaborate
        # TODO Add code coverage
        debug_str = " --debug all "
        cov_str = " "
    else: 
        cov_str = " -ignore_coverage "

    elaboration_log_path = cfg.sim_results_dir + "/" + lib_name + ".elab.log"
    add_elab_to_history_log(lib_name, elaboration_log_path)
    vivado.run_bin("xelab", top_dv_constructs_string + cov_str + debug_str + " " + args + " --incr -relax --O0 -v 0 -s " + top_dv_constructs[0] + " -timescale 1ns/1ps -L " + lib_name + "=./out/" + lib_name + " --log " + elaboration_log_path)
    
