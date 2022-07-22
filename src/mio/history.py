# Copyright 2022 Datum Technology Corporation
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
########################################################################################################################


import mio.cfg
import mio.clean
import mio.cmp
import mio.cov
import mio.dox
import mio.elab
import mio.results
import mio.sim
import mio.vivado
import mio.utilities


import os
import yaml


def create_history_log():
    if not os.path.exists(cfg.history_file_path):
        with open(cfg.history_file_path,'w') as yamlfile:
            yaml.dump({}, yamlfile)

