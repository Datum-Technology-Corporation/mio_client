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




def elab(ip_name):
    with open(mio.dv_path + "/" + ip_name + "/ip.yml", 'r') as yamlfile:
        dv_yaml = yaml.load(yamlfile, Loader=SafeLoader)
        if dv_yaml:
            top_hdl_unit = dv_yaml['hdl-src']['top-constructs'][0]
            do_elab(ip_name, top_hdl_unit)




def do_elab(lib_name, design_unit):
    
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
    
    if (mio.sim_cov):
        cov_str = " -cov_db_name " + design_unit + " -cov_db_dir " + pwd + "/results/cov"
    else: 
        cov_str = " -ignore_coverage "

    elaboration_log_path = mio.pwd + "/results/" + lib_name + ".elab.log"
    add_elab_to_history_log(lib_name, elaboration_log_path)
    mio.run_xsim_bin("xelab", lib_name + "." + design_unit + cov_str + debug_str + " --incr -relax --O0 -v 0 -s " + design_unit + " -timescale 1ns/1ps -L " + lib_name + "=./out/" + lib_name + " --log " + elaboration_log_path)
    
