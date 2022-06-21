# Copyright Datum Technology Corporation
########################################################################################################################
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
########################################################################################################################


import cfg
import clean
import cmp
import cov
import dox
import elab
import results
import sim
import vivado
import utilities


import os
import yaml


def create_history_log():
    if not os.path.exists(cfg.history_file_path):
        with open(cfg.history_file_path,'w') as yamlfile:
            yaml.dump({}, yamlfile)

