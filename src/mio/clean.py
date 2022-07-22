# Copyright 2022 Datum Technology Corporation
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
########################################################################################################################


import mio.cfg
import mio.cmp
import mio.cov
import mio.dox
import mio.elab
import mio.history
import mio.results
import mio.sim
import mio.vivado

import shutil
import os


def do_clean():
    if (cfg.dbg):
        print("Call to do_clean()")
    print("\033[1;31m********")
    print("Cleaning")
    print("********\033[0m")
    if os.path.exists(cfg.sim_results_dir + "/xsim.dir"):
        shutil.rmtree(cfg.sim_results_dir + "/xsim.dir")
    if os.path.exists(cfg.sim_results_dir + "/out"):
        shutil.rmtree(cfg.sim_results_dir + "/out")
    if os.path.exists(cfg.history_file_path):
        os.remove(cfg.history_file_path)
    history.create_history_log()


