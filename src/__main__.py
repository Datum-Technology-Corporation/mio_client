#! /usr/bin/python3 
# -*- coding: UTF-8 -*-
########################################################################################################################
## Copyright 2021 Datum Technology Corporation
## SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
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
  mio install <target>
  mio all     <target>  [-t <test_name>]  [-s <seed>]  [-v <level>]  [-g | --gui]  [-w | --waves]  [-q | --noclean]  [-c | --cov] [-- <args>]
  mio cmp     <target>
  mio elab    <target>  [-d | --debug]
  mio cpel    <target>
  mio sim     <target>  [-t <test_name>]  [-s <seed>]  [-v <level>]  [-g | --gui]  [-w | --waves]  [-c | --cov] [-- <args>]
  mio clean
  mio results    <target> <filename>
  mio cov        <target>
  mio dox <name> <target>
  mio install    <target>
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
import vivado
import install

from docopt     import docopt
import os
import subprocess
import shutil
import yaml
from datetime import datetime
from yaml.loader import SafeLoader
import re




def do_dispatch(args):
    cfg.glb_args = args
    
    if (cfg.dbg):
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
        cfg.glb_cfg['sim_waves'] = True
        cfg.glb_cfg['sim_debug'] = True
    else:
        cfg.glb_cfg['sim_waves'] = False
    
    if (args['-c'] or args['--cov']):
        cfg.glb_cfg['sim_debug'] = True
        cfg.glb_cfg['sim_cov'] = True
    else:
        cfg.glb_cfg['sim_cov'] = False
    
    if (args['-g'] or args['--gui']):
        cfg.glb_cfg['sim_debug'] = True
        cfg.glb_cfg['sim_gui'] = True
    else:
        cfg.glb_cfg['sim_gui'] = False
    
    if args['<args>'] == None:
        all_args = []
    else:
        all_args = re.sub("\"", "", args['<args>'])
        all_args = all_args.split()
    
    args_str = ""
    plus_args = []
    regex_pattern = "\+define\+((?:\w|_|\d)+(?:\=(?:\w|_|\d)+)?)"
    for arg in all_args:
        result = re.match(regex_pattern, arg)
        if result:
            define_arg = result.group(1)
            args_str = args_str + " --define " + define_arg # Only for vivado
        else:
            plus_args.append(arg)
    
    if args['clean']:
        clean.do_clean()
    if args['cmp']:
        out_path = cfg.pwd + "/out"
        if not os.path.exists(out_path):
            os.mkdir(out_path)
        cmp.cmp_rtl(args['<target>'], args_str)
        cmp.cmp_dv (args['<target>'], args_str)
    if args['elab']:
        elab.elab(args['<target>'], args_str)
    if args['sim']:
        sim.sim(args['<target>'], args['<test_name>'], args['<seed>'], args['<level>'], plus_args)
    if args['results']:
        results.do_parse_results(args['<target>'], args['<filename>'])
    if args['cov']:
        cov.gen_cov_report(args['<target>'])
    if args['dox']:
        dox.gen_doxygen(args['<name>'], args['<target>'])
    if args['install']:
        install.install_all_ips_for_target(args['<target>'])


if __name__ == '__main__':
    args = docopt(__doc__, version='Moore.io Client Command Line Interface - v0.1')
    if (cfg.dbg):
        print(args)
    do_dispatch(args)

