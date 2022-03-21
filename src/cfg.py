# Copyright Datum Technology Corporation
########################################################################################################################
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
########################################################################################################################


import clean
import cmp
import cov
import dox
import elab
import history
import results
import sim
import utilities
import vivado

import os


dbg             = False
sim_debug       = False
sim_gui         = False
sim_waves       = False
sim_cov         = False
glb_args = {}
glb_cfg  = {}

pwd               = os.getcwd()
temp_path         = pwd + '/temp'
vivado_path       = os.getenv("VIVADO", '/tools/vivado/2021.1/Vivado/2021.1/bin/')
uvm_dpi_so        = "uvm_dpi"
project_dir       = pwd + "/.."
rtl_path          = project_dir + "/rtl"
rtl_libs_path     = rtl_path + "/.imports"
dv_path           = project_dir + "/dv"
dv_imports_path   = dv_path + "/.imports"
history_file_path = pwd + "/history.yaml"
