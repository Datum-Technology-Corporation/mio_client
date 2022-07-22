# Copyright 2021-2022 Datum Technology Corporation
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
########################################################################################################################


import mio.clean
import mio.cmp
import mio.cov
import mio.dox
import mio.elab
import mio.history
import mio.results
import mio.sim
import mio.utilities
import mio.vivado

import jinja2
import os
import sys
import re

cli_args = None
dbg             = False
sim_debug       = False
sim_gui         = False
sim_waves       = False
sim_cov         = False
glb_args = {}
glb_cfg  = {}

mio_client_dir    = re.sub("cfg.py", "", os.path.realpath(__file__)) + ".."
mio_template_dir  = mio_client_dir + "/templates"
pwd               = os.getcwd()
temp_path         = pwd + '/temp'
vivado_path       = os.getenv("VIVADO_HOME", '/tools/vivado/2022.1/Vivado/2022.1/bin/')
uvm_dpi_so        = "uvm_dpi"
project_dir       = pwd + "/.."
project_name      = ""
user_dir          = os.path.expanduser("~")
sim_dir           = project_dir + "/sim"
sim_results_dir   = sim_dir + "/results"
ip_paths          = {}
mio_user_dir      = "~/.mio"
user_global_ips_path = mio_user_dir + "/vendors"
mio_data_dir      = project_dir + "/.mio"
sim_output_dir    = mio_data_dir + "/sim_out"
dependencies_path = mio_data_dir + "/vendors"
ip_cache_file     = mio_data_dir + "/ip_cache.yml"
history_file_path = mio_data_dir + "/history.yml"
rtl_path          = project_dir + "/rtl"
rtl_libs_path     = rtl_path + "/.imports"
dv_path           = project_dir + "/dv"
dv_imports_path   = dv_path + "/.imports"
test_results_path_template = "{{ ip_name }}_{{ test_name }}_{{ seed }}"

templateLoader = jinja2.FileSystemLoader(searchpath=mio_template_dir)
templateEnv    = jinja2.Environment(loader=templateLoader)

configuration = {}
