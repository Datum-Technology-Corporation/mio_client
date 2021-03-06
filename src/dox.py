# Copyright Datum Technology Corporation
########################################################################################################################
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
########################################################################################################################


import subprocess


def gen_doxygen(name, path_in):
    args = "SRC_PATH=" + path_in + " MIO_HOME=${MIO_HOME} IP_NAME=" + name
    subprocess.call(args + " doxygen ../dv/" + name + "/bin/doxygen.cfg", shell=True)
