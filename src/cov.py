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


#xcrg  -dir a1  -dir b1  -db_name d1  -db_name   d2  -merge_dir    m1   -merge_db_name   n1 -log result.txt  -report_format   html  -report_dir    report1
def gen_cov_report(cfg, sim_lib):
    print("Generating coverage report for " + sim_lib)
    # TODO Bring back coverage merge once it is done per sim
    dir_string = ""
    db_name_string = ""
    merge_string = "-merge_dir " + mio.pwd + "/cov/merge" + " -merge_db_name " + sim_lib
    now = datetime.now()
    timestamp = now.strftime("%Y/%m/%d-%H:%M:%S")
    print("Parsing results ...")
    if not os.path.exists(mio.history_file_path):
        sys.exit("No history log file")
    else:
        with open(mio.history_file_path,'r') as yamlfile:
            cur_yaml = yaml.load(yamlfile, Loader=SafeLoader)
            if not cur_yaml:
                sys.exit("Failed to open history log file")
            else:
                if not 'simulations' in cur_yaml[sim_lib]:
                    sys.exit("No record of simulations for " + sim_lib)
                else:
                    for sim in cur_yaml[sim_lib]['simulations']:
                        cov_path = sim + "/cov"
                        if cur_yaml[sim_lib]['simulations'][sim]['cov']:
                            dir_string     = dir_string + " -dir " + cov_path
                            db_name_string = db_name_string + " -db_name " + cur_yaml[sim_lib]['simulations'][sim]['test_name'] + "_" + cur_yaml[sim_lib]['simulations'][sim]['seed']
    
    if not os.path.exists(mio.pwd + "/cov"):
        os.mkdir(mio.pwd + "/cov")
    if not os.path.exists(mio.pwd + "/cov/reports"):
        os.mkdir(mio.pwd + "/cov/reports")
    mio.run_xsim_bin("xcrg", dir_string + " " + db_name_string + " " + merge_string + " -report_format text -report_dir " + mio.pwd + "/cov/reports/" + sim_lib)

