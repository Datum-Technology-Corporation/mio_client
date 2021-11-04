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
import mio
import yaml
from yaml.loader import SafeLoader
from datetime import datetime


def add_cmp_to_history_log(snapshot, compilation_log_path):
    now = datetime.now()
    timestamp = now.strftime("%Y/%m/%d-%H:%M:%S")
    if not os.path.exists(mio.history_file_path):
        mio.create_history_log()
    with open(mio.history_file_path,'r') as yamlfile:
        cur_yaml = yaml.load(yamlfile, Loader=SafeLoader) # Note the safe_load
        if not snapshot in cur_yaml:
            cur_yaml[snapshot] = {}
        cur_yaml[snapshot]['compilation_timestamp'] = timestamp
        cur_yaml[snapshot]['compilation_log_path'] = compilation_log_path
        if cur_yaml:
            with open(mio.history_file_path,'w') as yamlfile:
                yaml.dump(cur_yaml, yamlfile) # Also note the safe_dump




def do_cmp_rtl(target_design):
    if (dbg):
        print("Call to do_cmp_rtl(target_design='" + target_design + "'")
    




def cmp_rtl(ip_name):
    with open(mio.dv_path + "/" + ip_name + "/ip.yml", 'r') as yamlfile:
        dv_yaml = yaml.load(yamlfile, Loader=SafeLoader)
        if dv_yaml:
            if 'dut-ip' in dv_yaml['hdl-src']:
                rtl_ip_name = dv_yaml['hdl-src']['dut-ip']
                with open(mio.rtl_path + "/" + rtl_ip_name + "/ip.yml", 'r') as yamlfile:
                    rtl_yaml = yaml.load(yamlfile, Loader=SafeLoader)
                    if rtl_yaml:
                        rtl_sub_type = rtl_yaml['ip']['sub-type'].lower().strip()
                        if (rtl_sub_type == "vivado"):
                            rtl_lib_name = rtl_yaml['hdl-src']['lib-name']
                            xilinx_libs  = rtl_yaml['hdl-src']['xilinx-libs']
                            vlog_prj_file_path = rtl_yaml['hdl-src']['vlog']
                            vhdl_prj_file_path = rtl_yaml['hdl-src']['vhdl']
                            vlog_compilation_log_path = mio.pwd + "/results/" + rtl_ip_name + ".vlog.cmp.log"
                            vhdl_compilation_log_path = mio.pwd + "/results/" + rtl_ip_name + ".vhdl.cmp.log"
                            print("\033[1;35m*************")
                            print("Compiling RTL")
                            print("*************\033[0m")
                            mio.run_xsim_bin("xvlog", " --relax -prj " + mio.rtl_path + "/" + rtl_ip_name + "/" + vlog_prj_file_path + " --log " + vlog_compilation_log_path)
                            mio.run_xsim_bin("xvhdl", " --relax -prj " + mio.rtl_path + "/" + rtl_ip_name + "/" + vhdl_prj_file_path + " --log " + vhdl_compilation_log_path)
                            add_cmp_to_history_log(rtl_lib_name + ".vlog", vlog_compilation_log_path)
                            add_cmp_to_history_log(rtl_lib_name + ".vhdl", vhdl_compilation_log_path)
                        else:
                            print("Compilation of non-vivado RTL projects is not yet supported")




def cmp_dv(ip_name):
    with open(mio.dv_path + "/" + ip_name + "/ip.yml", 'r') as yamlfile:
        dv_yaml = yaml.load(yamlfile, Loader=SafeLoader)
        if dv_yaml:
            filelist_path = mio.dv_path + "/" + ip_name + "/" + dv_yaml['hdl-src']['flists']['vivado'][0]
        do_cmp_dv(filelist_path, ip_name)




def do_cmp_dv(filelist_path, lib_name):
    if (mio.dbg):
        print("Call to do_cmp_dv(filelist_path='" + filelist_path + "', lib_name='" + lib_name + "')")
    print("\033[0;36m************")
    print("Compiling DV")
    print("************\033[0m")
    if not os.path.exists(mio.pwd + "/results"):
        os.mkdir(mio.pwd + "/results")
    compilation_log_path = mio.pwd + "/results/" + lib_name + ".cmp.log"
    add_cmp_to_history_log(lib_name, compilation_log_path)
    mio.run_xsim_bin("xvlog", "--incr -sv -f " + filelist_path + " -L uvm --work " + lib_name + "=./out/" + lib_name + " --log " + compilation_log_path)
