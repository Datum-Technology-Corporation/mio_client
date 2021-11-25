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


import yaml
from yaml.loader import SafeLoader
from datetime import datetime
import mio
import os


def add_elab_to_history_log(snapshot, elaboration_log_path):
    now = datetime.now()
    timestamp = now.strftime("%Y/%m/%d-%H:%M:%S")
    if not os.path.exists(mio.history_file_path):
        create_history_log()
    with open(mio.history_file_path,'r') as yamlfile:
        cur_yaml = yaml.load(yamlfile, Loader=SafeLoader) # Note the safe_load
        if not snapshot in cur_yaml:
            cur_yaml[snapshot] = {}
        cur_yaml[snapshot]['elaboration_timestamp'] = timestamp
        cur_yaml[snapshot]['elaboration_log_path'] = elaboration_log_path
    if cur_yaml:
        with open(mio.history_file_path,'w') as yamlfile:
            yaml.dump(cur_yaml, yamlfile) # Also note the safe_dump




def elab(cfg, ip_name):
    with open(mio.dv_path + "/" + ip_name + "/ip.yml", 'r') as yamlfile:
        dv_yaml = yaml.load(yamlfile, Loader=SafeLoader)
        if dv_yaml:
            if 'dut-ip' in dv_yaml['hdl-src']:
                rtl_ip_name = dv_yaml['hdl-src']['dut-ip']
                top_dv_constructs = dv_yaml['hdl-src']['top-constructs']
                if (rtl_ip_name):
                    with open(mio.rtl_path + "/" + rtl_ip_name + "/ip.yml", 'r') as yamlfile:
                        rtl_yaml = yaml.load(yamlfile, Loader=SafeLoader)
                        if rtl_yaml:
                            rtl_sub_type = rtl_yaml['ip']['sub-type'].lower().strip()
                            if (rtl_sub_type == "vivado"):
                                rtl_lib_name = rtl_yaml['hdl-src']['lib-name']
                                xilinx_libs  = rtl_yaml['hdl-src']['xilinx-libs']
                                top_rtl_constructs = rtl_yaml['hdl-src']['top-constructs']
                                do_dut_vivado_elab(cfg, ip_name, rtl_lib_name, xilinx_libs, top_dv_constructs, top_rtl_constructs)
                            else:
                                print("Elaboration of non-Vivado RTL Project DUTs is not yet supported")
            else:
                top_hdl_unit = dv_yaml['hdl-src']['top-constructs'][0]
                do_elab(cfg, ip_name, top_hdl_unit)




def do_dut_vivado_elab(cfg, ip_name, lib_name, xilinx_libs, top_dv_constructs, top_rtl_constructs):
    elaboration_log_path = mio.pwd + "/results/" + lib_name + ".elab.log"
    lib_string = ""
    top_rtl_constructs_string = ""
    for construct in top_rtl_constructs:
        top_rtl_constructs_string = top_rtl_constructs_string + " " + construct
    for lib in xilinx_libs:
        lib_string = lib_string + " -L " + lib
    mio.run_xsim_bin("xelab", " --relax -debug all --mt auto -L " + ip_name + "=./out/" + ip_name + " -L " + lib_name + lib_string + " --snapshot " + top_dv_constructs[0] + " " + ip_name + "." + top_dv_constructs[0] + " " + top_rtl_constructs_string + " --log " + elaboration_log_path)
    add_elab_to_history_log(ip_name, elaboration_log_path)
    




def do_elab(cfg, lib_name, design_unit):
    
    debug_str = ""

    if (mio.dbg):
        print("Call to do_elab(lib_name='" + lib_name + "', design_unit='" + design_unit + "')")
    print("\033[0;36m***********")
    print("Elaborating")
    print("***********\033[0m")
    
    if (mio.sim_debug):
        debug_str = " --debug all "
    else:
        debug_str = " --debug typical "
    
    if (cfg['sim_cov'] == True):
        # TODO Move this to sim, not elaborate
        # TODO Add code coverage
        debug_str = " --debug all "
        cov_str = " -cov_db_name " + lib_name + " -cov_db_dir cov"
    else: 
        cov_str = " -ignore_coverage "

    elaboration_log_path = mio.pwd + "/results/" + lib_name + ".elab.log"
    add_elab_to_history_log(lib_name, elaboration_log_path)
    mio.run_xsim_bin("xelab", lib_name + "." + design_unit + cov_str + debug_str + " --incr -relax --O0 -v 0 -s " + design_unit + " -timescale 1ns/1ps -L " + lib_name + "=./out/" + lib_name + " --log " + elaboration_log_path)
    
