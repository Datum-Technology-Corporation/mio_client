# Copyright 2022 Datum Technology Corporation
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
########################################################################################################################


import mio.cfg
import mio.clean
import mio.cmp
import mio.cov
import mio.dox
import mio.elab
import mio.history
import mio.results
import mio.sim
import mio.vivado

import os
import yaml


def set_env_var(name, value):
    if (cfg.dbg):
        print("Setting env var '" + name + "' to value '" + value + "'")
    os.environ[name] = value


def copy_tree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def create_history_log():
    if not os.path.exists(cfg.history_file_path):
        if cfg.dbg:
            print("Creating history.yaml file at " + cfg.history_file_path)
        with open(cfg.history_file_path, 'w') as yamlfile:
            yaml.dump({}, yamlfile)

