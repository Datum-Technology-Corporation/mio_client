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


"""Moore.io Command Line Interface (CLI) Client.

                              ███╗   ███╗ ██████╗  ██████╗ ██████╗ ███████╗   ██╗ ██████╗
                              ████╗ ████║██╔═══██╗██╔═══██╗██╔══██╗██╔════╝   ██║██╔═══██╗
                              ██╔████╔██║██║   ██║██║   ██║██████╔╝█████╗     ██║██║   ██║
                              ██║╚██╔╝██║██║   ██║██║   ██║██╔══██╗██╔══╝     ██║██║   ██║
                              ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██║  ██║███████╗██╗██║╚██████╔╝
                              ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚═╝ ╚═════╝
                            Moore.io (`mio`) Command Line Interface (CLI) - Pre-Beta Edition

               NOTE: THE FOLLOWING INTERFACE DEFINITION WILL BE SUBJECT TO DEPRECATION IN THE NEAR FUTURE
                     IN FAVOR OF A MUCH LARGER, FAR BETTER ENCOMPASSING VERSION:
                           https://github.com/Datum-Technology-Corporation/mio_cli/tree/main/mio/cli

Usage:
  mio all  <target>  [-t <test_name>]  [-s <seed>]  [-v <level>]  [-g | --gui]  [-w | --waves]  [-q | --noclean]  [-c | --cov] [-- <args>]
  mio cmp  <target>
  mio elab <target>  [-d | --debug]
  mio cpel <target>
  mio sim  <target>  [-t <test_name>]  [-s <seed>]  [-v <level>]  [-g | --gui]  [-w | --waves]  [-c | --cov] [-- <args>]
  mio clean
  mio results    <target> <filename>
  mio cov        <target>
  mio dox <name> <target>
  mio (-h | --help)
  mio --version

Options:
  -h --help     Show this screen.
  --version     Show version.
   
Examples:
  mio clean                          # Deletes all simulation artifacts and results
  
  mio cmp  uvmt_my_ip                # Only compile test bench for uvmt_my_ip
  mio elab uvmt_my_ip                # Only elaborate test bench for uvmt_my_ip
  mio cpel uvmt_my_ip                # Compile and elaborate test bench for uvmt_my_ip
  mio sim  uvmt_my_ip -t smoke -s 1  # Only simulates test 'uvmt_my_ip_smoke_test_c' for top-level module 'uvmt_my_ip_tb'
  
  mio all uvmt_my_ip -t smoke -s 1   # Compiles, elaborates and simulates test 'uvmt_my_ip_smoke_test_c' for bench 'uvmt_my_ip'
"""


import clean
import cmp
import cov
import dox
import elab
import results
import sim
from docopt     import docopt
import os
import subprocess
import shutil
import yaml
from datetime import datetime
from yaml.loader import SafeLoader
import re


dbg             = False
sim_debug       = False
sim_gui         = False
sim_waves       = False
sim_cov         = False
glb_args = {}
glb_cfg = {}

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


def do_dispatch(args):
    global sim_debug
    global sim_gui
    global sim_waves
    global sim_cov
    global glb_args
    global glb_cfg
    
    glb_args = args
    
    if (dbg):
        print("Call to do_dispatch()")
    
    if not args['<seed>']:
        args['<seed>'] = 1
    
    if args['results']:
        args['clean'] = False
        args['cmp'  ] = False
        args['elab' ] = False
        args['sim'  ] = False
    
    if args['all']:
        args['cmp'  ] = True
        args['elab' ] = True
        args['sim'  ] = True
        if (args['-q'] or args['--noclean']):
            args['clean'] = False
        else:
            args['clean'] = True
    
    if args['cpel']:
        args['clean'] = True
        args['cmp'  ] = True
        args['elab' ] = True
        args['sim'  ] = False
    
    if (args['-w'] or args['--waves']):
        glb_cfg['sim_waves'] = True
        glb_cfg['sim_debug'] = True
    else:
        glb_cfg['sim_waves'] = False
    
    if (args['-c'] or args['--cov']):
        glb_cfg['sim_debug'] = True
        glb_cfg['sim_cov'] = True
    else:
        glb_cfg['sim_cov'] = False
    
    if (args['-g'] or args['--gui']):
        glb_cfg['sim_debug'] = True
        glb_cfg['sim_gui'] = True
    else:
        glb_cfg['sim_gui'] = False
    
    if args['<args>'] == None:
        final_args = []
    else:
        final_args = args['<args>'].split()
    
    if args['clean']:
        clean.do_clean()
    if args['cmp']:
        out_path = pwd + "/out"
        if not os.path.exists(out_path):
            os.mkdir(out_path)
        cmp.cmp_rtl(glb_cfg, args['<target>'])
        cmp.cmp_dv (glb_cfg, args['<target>'])
    if args['elab']:
        elab.elab(glb_cfg, args['<target>'])
    if args['sim']:
        sim.sim(glb_cfg, args['<target>'], args['<test_name>'], args['<seed>'], args['<level>'], final_args)
    if args['results']:
        results.do_parse_results(args['<target>'], args['<filename>'])
    if args['cov']:
        cov.gen_cov_report(glb_cfg, args['<target>'])
    if args['dox']:
        dox.gen_doxygen(args['<name>'], args['<target>'])


def set_env_var(name, value):
    if (dbg):
        print("Setting env var '" + name + "' to value '" + value + "'")
    os.environ[name] = value


def create_history_log():
    if not os.path.exists(history_file_path):
        with open(history_file_path,'w') as yamlfile:
            yaml.dump({}, yamlfile)


def copy_tree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def run_xsim_bin(name, args):
    bin_path = vivado_path + name
    if (dbg):
        print("Call to run_xsim_bin(name='" + name + "', args='"  + args + "')")
        print("System call is " + bin_path + " " + args)
    subprocess.call(bin_path + " " + args, shell=True)


if __name__ == '__main__':
    args = docopt(__doc__, version='DVMake 0.1')
    if (dbg):
        print(args)
    do_dispatch(args)

