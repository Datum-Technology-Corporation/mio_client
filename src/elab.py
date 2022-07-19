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

import re
import yaml
from yaml.loader import SafeLoader
from datetime import datetime
#import mio
import os


def add_elab_to_history_log(snapshot, elaboration_log_path):
    now = datetime.now()
    timestamp = now.strftime("%Y/%m/%d-%H:%M:%S")
    if not os.path.exists(cfg.history_file_path):
        create_history_log()
    with open(cfg.history_file_path,'r') as yamlfile:
        cur_yaml = yaml.load(yamlfile, Loader=SafeLoader) # Note the safe_load
        if not snapshot in cur_yaml:
            cur_yaml[snapshot] = {}
        cur_yaml[snapshot]['elaboration_timestamp'] = timestamp
        cur_yaml[snapshot]['elaboration_log_path'] = elaboration_log_path
    if cur_yaml:
        with open(cfg.history_file_path,'w') as yamlfile:
            yaml.dump(cur_yaml, yamlfile) # Also note the safe_dump




def elab(ip_name, args):
    with open(cfg.dv_path + "/" + ip_name + "/ip.yml", 'r') as yamlfile:
        dv_yaml = yaml.load(yamlfile, Loader=SafeLoader)
        if dv_yaml:
            if 'dut' in dv_yaml:
                rtl_ip_name = dv_yaml['dut']['name']
                rtl_ip_type = dv_yaml['dut']['ip-type']
                top_dv_constructs = dv_yaml['hdl-src']['top-constructs']
                
                if (rtl_ip_type == "mio"):
                    if os.path.exists(cfg.rtl_path + "/" + rtl_ip_name): # Search for IP in RTL dir
                        ip_dir = cfg.rtl_path + "/" + rtl_ip_name
                    elif os.path.exists(cfg.rtl_path + "/.imports/" + rtl_ip_name): # If not found, look in .imports dir
                        ip_dir = cfg.rtl_path + "/.imports/" + rtl_ip_name
                    else:
                        print("ERROR: Could not find DUT IP " + rtl_ip_name)
                        return
                    with open(cfg.rtl_path + "/" + rtl_ip_name + "/ip.yml", 'r') as yamlfile:
                        rtl_yaml = yaml.load(yamlfile, Loader=SafeLoader)
                        if rtl_yaml:
                            rtl_sub_type = rtl_yaml['ip']['sub-type'].lower().strip()
                            if (rtl_sub_type == "vivado"):
                                rtl_lib_name = rtl_yaml['hdl-src']['lib-name']
                                xilinx_libs  = rtl_yaml['hdl-src']['xilinx-libs']
                                top_rtl_constructs = rtl_yaml['hdl-src']['top-constructs']
                                do_dut_vivado_elab(ip_name, rtl_lib_name, xilinx_libs, top_dv_constructs, top_rtl_constructs, args)
                            else:
                                print("ERROR: Elaboration of non-Vivado RTL Project DUTs is not yet supported")
                elif (rtl_ip_type == "fsoc"):
                    fsoc_fname  = dv_yaml['dut']['full-name']
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
                top_hdl_unit = dv_yaml['hdl-src']['top-constructs']
                do_elab(ip_name, top_hdl_unit, args)





def do_dut_vivado_elab(ip_name, lib_name, xilinx_libs, top_dv_constructs, top_rtl_constructs, args):
    print("\033[0;36m***********")
    print("Elaborating")
    print("***********\033[0m")
    elaboration_log_path = cfg.pwd + "/results/" + lib_name + ".elab.log"
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
        top_dv_constructs_string = top_dv_constructs_string + " " + ip_name + "." + construct
    print("\033[0;36m***********")
    print("Elaborating")
    print("***********\033[0m")
    elaboration_log_path = cfg.pwd + "/results/" + lib_name + ".elab.log"
    vivado.run_bin("xelab", " --incr -dup_entity_as_module -relax -debug all " + args + " --O0 -v 0 -timescale 1ns/1ps -L " + ip_name + "=./out/" + ip_name + " -L " + lib_name + "=./out/" + lib_name + " --snapshot " + top_dv_constructs[0] + " " + top_dv_constructs_string + " --log " + elaboration_log_path)
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

    elaboration_log_path = cfg.pwd + "/results/" + lib_name + ".elab.log"
    add_elab_to_history_log(lib_name, elaboration_log_path)
    vivado.run_bin("xelab", top_dv_constructs_string + cov_str + debug_str + " " + args + " --incr -relax --O0 -v 0 -s " + top_dv_constructs[0] + " -timescale 1ns/1ps -L " + lib_name + "=./out/" + lib_name + " --log " + elaboration_log_path)
    
