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
from datetime import datetime


def gen_cov_report(sim_lib):
    print("Generating coverage report for " + sim_lib)
    # TODO Bring back coverage merge once it is done per sim
    #dir_string = ""
    #now = datetime.now()
    #timestamp = now.strftime("%Y/%m/%d-%H:%M:%S")
    #print("Parsing results ...")
    #if not os.path.exists(mio.history_file_path):
    #    sys.exit("No history log file")
    #else:
    #    with open(mio.history_file_path,'r') as yamlfile:
    #        cur_yaml = yaml.load(yamlfile, Loader=SafeLoader)
    #        if cur_yaml:
    #            for sim in cur_yaml[sim_lib]['simulations']:
    #                cov_path = sim + "/cov/xsim.covdb"
    #                if cur_yaml[sim_lib]['simulations'][sim]['cov']:
    #                    dir_string = dir_string + " -dir " + cov_path
    
    if not os.path.exists(mio.pwd + "/cov_report"):
        os.mkdir(mio.pwd + "/cov_report")
    mio.run_xsim_bin("xcrg", "-report_format text -report_dir . -db_name " + sim_lib + " -dir cov")

