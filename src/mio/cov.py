# Copyright 2022 Datum Technology Corporation
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
########################################################################################################################


import mio.cfg
import mio.clean
import mio.cmp
import mio.dox
import mio.elab
import mio.history
import mio.results
import mio.sim
import mio.vivado

import os
import yaml
from yaml.loader import SafeLoader
from datetime import datetime


#xcrg  -dir a1  -dir b1  -db_name d1  -db_name   d2  -merge_dir    m1   -merge_db_name   n1 -log result.txt  -report_format   html  -report_dir    report1
def gen_cov_report(sim_lib):
    print("Generating coverage report for " + sim_lib)
    # TODO Bring back coverage merge once it is done per sim
    dir_string = ""
    db_name_string = ""
    merge_string = "-merge_dir " + cfg.sim_dir + "/cov/merge" + " -merge_db_name " + sim_lib
    now = datetime.now()
    timestamp = now.strftime("%Y/%m/%d-%H:%M:%S")
    print("Parsing results ...")
    if not os.path.exists(cfg.history_file_path):
        sys.exit("No history log file")
    else:
        with open(cfg.history_file_path,'r') as yamlfile:
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
    
    if not os.path.exists(cfg.sim_dir + "/cov"):
        os.mkdir(cfg.sim_dir + "/cov")
    if not os.path.exists(cfg.sim_dir + "/cov/reports"):
        os.mkdir(cfg.sim_dir + "/cov/reports")
    vivado.run_bin("xcrg", dir_string + " " + db_name_string + " " + merge_string + " -report_format text -report_dir " + cfg.sim_dir + "/cov/reports/" + sim_lib)

