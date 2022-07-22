########################################################################################################################
# Copyright 2021-2022 Datum Technology Corporation
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
########################################################################################################################


"""
                              ███╗   ███╗ ██████╗  ██████╗ ██████╗ ███████╗   ██╗ ██████╗
                              ████╗ ████║██╔═══██╗██╔═══██╗██╔══██╗██╔════╝   ██║██╔═══██╗
                              ██╔████╔██║██║   ██║██║   ██║██████╔╝█████╗     ██║██║   ██║
                              ██║╚██╔╝██║██║   ██║██║   ██║██╔══██╗██╔══╝     ██║██║   ██║
                              ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██║  ██║███████╗██╗██║╚██████╔╝
                              ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚═╝ ╚═════╝
                                  Moore.io (`mio`) Command Line Interface (CLI) - v1p0
Usage:
  mio install <ip>
  mio all     <ip>  [-t <test_name>]  [-s <seed>]  [-v <level>]  [-g | --gui]  [-w | --waves]  [-q | --noclean]  [-c | --cov] [-- <args>]
  mio cmp     <ip>
  mio elab    <ip>  [-d | --debug]
  mio cpel    <ip>
  mio sim     <ip>  [-C] [-E] [-S] [-t <test_name>]  [-s <seed>]  [-v <level>]  [-g | --gui]  [-w | --waves]  [-c | --cov] [-- <args>]
  mio clean
  mio results    <ip> <filename>
  mio cov        <ip>
  mio dox        <ip>
  mio install    <ip> [-g | --global]  [-u <username>]  [-p <password>]
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



import mio.cfg
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
import mio.install
import mio.discovery

import sys
from docopt     import docopt
import os
import subprocess
import shutil
import yaml
from datetime import datetime
from yaml.loader import SafeLoader
import re




def do_dispatch():
    args = cfg.glb_args
    
    if (cfg.dbg):
        print("Call to do_dispatch()")
    
    discovery.find_project_toml_file()
    discovery.load_configuration()
    discovery.catalog_ips()
    discovery.set_env_vars()
    
    if not args['<seed>']:
        args['<seed>'] = 1
    
    if args['results']:
        args['clean'] = False
        args['cmp'  ] = False
        args['elab' ] = False
        args['sim'  ] = False
    
    if args['sim']:
        if not args['-C'] and not args['-E'] and not args['-S']:
            # TODO Add IP cache and use info to only build what is necessary
            args['cmp'  ] = True
            args['elab' ] = True
            args['sim'  ] = True
        else:
            if args['-C']:
                args['cmp'  ] = True
            else:
                args['cmp'  ] = False
            if args['-E']:
                args['elab' ] = True
            else:
                args['elab' ] = False
            if args['-S']:
                args['sim' ] = True
            else:
                args['sim' ] = False
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
    
    if 'sim_debug' not in cfg.glb_cfg:
        cfg.glb_cfg['sim_debug'] = False
    
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
        cmp.cmp_rtl(args['<ip>'], args_str)
        cmp.cmp_dv (args['<ip>'], args_str)
    if args['elab']:
        elab.elab(args['<ip>'], args_str)
    if args['sim']:
        sim.sim(args['<ip>'], args['<test_name>'], args['<seed>'], args['<level>'], plus_args)
    if args['results']:
        results.do_parse_results(args['<ip>'], args['<filename>'])
    if args['cov']:
        cov.gen_cov_report(args['<ip>'])
    if args['dox']:
        dox.gen_doxygen(args['<ip>'])
    if args['install']:
        if args['--global'] or args['-g']:
            args['--global'] = True
        install.install_all_ips_for_target(args['<ip>'], args['--global'], args['<username>'], args['<password>'])


def main():
    cfg.glb_args = docopt(argv=sys.argv,doc=__doc__, version='Moore.io Client Command Line Interface - v0.1')
    if (cfg.dbg):
        print(cfg.glb_args)
    do_dispatch()

