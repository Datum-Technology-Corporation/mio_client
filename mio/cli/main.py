##
## Copyright 2021 Datum Technology Corporation
## SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
## 
## Licensed under the Solderpad Hardware License v 2.1 (the "License"); you may
## not use this file except in compliance with the License, or, at your option,
## the Apache License version 2.0. You may obtain a copy of the License at
## 
##     https://solderpad.org/licenses/SHL-2.1/
## 
## Unless required by applicable law or agreed to in writing, any work
## distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
## WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
## License for the specific language governing permissions and limitations
## under the License.
##


########################################################################################################################
# IMPORTS
########################################################################################################################
from docopt import docopt
from art import *
import sys
import logging
from . import clean
from . import completion
from . import config
from . import doctor
from . import emul
from . import formal
from . import hdl_connect
from . import hdl_doc
from . import hdl_refactor
from . import hdl_style
from . import help_search
from . import help
from . import init
from . import ip
from . import lint
from . import new
from . import org
from . import regr
from . import results
from . import run_script
from . import set_script
from . import sim
from . import timing
from . import synth
from . import team
from . import user
from . import vcs
########################################################################################################################


__doc__ = f"""                                     {help.cli_title}
                                           I N T E R A C T I V E   D E M O

{help.cli_usage}

{help.cli_partial_command_list}"""

commands = f"""{help.cli_title}

{help.cli_full_command_list}"""


########################################################################################################################
# GLOBAL VARIABLES
########################################################################################################################
mio_version = '0.1.0.0'
########################################################################################################################


########################################################################################################################
# TOP-LEVEL FUNCTIONS
########################################################################################################################
def proccess_args():
    args = docopt(__doc__, options_first=True, version=False, help=False)
    argv = [args['<command>']] + args['<args>']
    debug = 0
    if '--dbg' in args:
        try:
            debug = int(args['--dbg'])
        except ValueError:
            sys.exit(str(ValueError))
        except TypeError:
            debug = 0
        else:
            debug *= 10
            if debug > 0:
                print("Setting debug level to {}".format(debug))
                logging.Logger.setLevel(logging.getLogger(), debug)

    logging.debug('global arguments:\n' + str(args))
    logging.debug('command arguments:\n' + str(argv))

    process_help(args, argv)
    process_version(args, argv)
    process_list_commands(args, argv)
    process_html_path(args, argv)
    process_man_path(args, argv)
    process_info_path(args, argv)
    process_command(args, argv, debug)


def process_version(args, argv):
    print_version_info = False
    if '-v' in args and args['-v']:
        print_version_info = True

    if not print_version_info:
        if '--version' in args and args['--version']:
            print_version_info = True

    if print_version_info:
        print_version()
        exit()


def process_help(args, argv):
    print_help_info = False
    if '-h' in args and args['-h']:
        print_help_info = True
    
    if not print_help_info:
        if '--help' in args and args['--help']:
            print_help_info = True
    
    if print_help_info:
        print_help()
        exit()


def process_list_commands(args, argv):
    if '--list-commands' in args and args['--list-commands']:
        print_list_of_commands()
        exit()


def process_html_path(args, argv):
    if '--html-path' in args and args['--html-path']:
        print_html_path()
        exit()


def process_man_path(args, argv):
    if '--man-path' in args and args['--man-path']:
        print_man_path()
        exit()


def process_info_path(args, argv):
    if '--info-path' in args and args['--info-path']:
        print_info_path()
        exit()


def process_command(args, argv, debug):
    if args['<command>'] == 'clean':
        clean.main(argv)
    elif args['<command>'] == 'completion':
        completion.main(argv)
    elif args['<command>'] == 'config':
        config.main(argv)
    elif args['<command>'] == 'doctor':
        doctor.main(argv)
    elif args['<command>'] == 'emulate':
        emulate.main(argv)
    elif args['<command>'] == 'formal':
        formal.main(argv)
    elif args['<command>'] == 'hdl-connect':
        hdl_connect.main(argv)
    elif args['<command>'] == 'hdl-doc':
        hdl_doc.main(argv)
    elif args['<command>'] == 'hdl-refactor':
        hdl_refactor.main(argv)
    elif args['<command>'] == 'hdl-style':
        hdl_style.main(argv)
    elif args['<command>'] == 'help-search':
        help_search.main(argv)
    elif args['<command>'] == 'help':
        help.main(argv)
    elif args['<command>'] == 'init':
        init.main(argv)
    elif args['<command>'] == 'ip':
        ip.main(argv)
    elif args['<command>'] == 'lint':
        lint.main(argv)
    elif args['<command>'] == 'new':
        new.main(argv)
    elif args['<command>'] == 'org':
        org.main(argv)
    elif args['<command>'] == 'regr':
        regr.main(argv)
    elif args['<command>'] == 'results':
        results.main(argv)
    elif args['<command>'] == 'run-script':
        run_script.main(argv)
    elif args['<command>'] == 'set-script':
        set_script.main(argv)
    elif args['<command>'] == 'sim':
        sim.main(argv)
    elif args['<command>'] == 'synth':
        synth.main(argv)
    elif args['<command>'] == 'team':
        team.main(argv)
    elif args['<command>'] == 'timing':
        timing.main(argv)
    elif args['<command>'] == 'user':
        user.main(argv)
    elif args['<command>'] == 'vcs':
        vcs.main(argv)
    else:
        exit_error(args, argv, debug)


def exit_error(args, argv, debug):
    exit("'{}' is not an mio command. See 'mio --list-commands'."
             .format(args['<command>']))


def feature_not_supported():
    exit("Feature not yet supported.")


def print_help():
    #print(text2art("Moore.io", "ticks"))
    print(help.logo)
    print(__doc__)


def print_version():
    print(mio_version)


def print_list_of_commands():
    print(commands)


def print_html_path():
    feature_not_supported()


def print_man_path():
    feature_not_supported()


def print_info_path():
    feature_not_supported()
########################################################################################################################
