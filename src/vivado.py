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
import history
import results
import sim
import utilities

import subprocess


def run_bin(name, args):
    bin_path = cfg.vivado_path + name
    if (cfg.dbg):
        print("Call to run_xsim_bin(name='" + name + "', args='"  + args + "')")
        print("System call is " + bin_path + " " + args)
    subprocess.call(bin_path + " " + args, shell=True)
