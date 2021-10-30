# Copyright 2021 Datum Technology Corporation
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
########################################################################################################################
# Licensed under the Solderpad Hardware License v 2.1 (the "License"); you may not use this file except in compliance
# with the License, or, at your option, the Apache License version 2.0.  You may obtain a copy of the License at
#                                       https://solderpad.org/licenses/SHL-2.1/
# Unless required by applicable law or agreed to in writing, any work distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.
########################################################################################################################


"""Moore.io Help Command
   Shows the appropriate documentation page for the specified command

Usage: mio help <command> [<subcommand>]

Examples:
   mio help sim
   mio help ip install
   mio help mio"""


logo = """                              ███╗   ███╗ ██████╗  ██████╗ ██████╗ ███████╗   ██╗ ██████╗
                              ████╗ ████║██╔═══██╗██╔═══██╗██╔══██╗██╔════╝   ██║██╔═══██╗
                              ██╔████╔██║██║   ██║██║   ██║██████╔╝█████╗     ██║██║   ██║
                              ██║╚██╔╝██║██║   ██║██║   ██║██╔══██╗██╔══╝     ██║██║   ██║
                              ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██║  ██║███████╗██╗██║╚██████╔╝
                              ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚═╝ ╚═════╝ """

cli_title = "Moore.io (`mio`) Command Line Interface (CLI)"

cli_usage = """Usage:
   mio [--version] [--help] [--list-commands]
   mio [--html-path] [--man-path] [--info-path]
   mio [--wd=<path>] [--config=<name>=<value>] [--config-env=<name>=<envvar>]
       [-p | --paginate | -P | --no-pager]
       [--dbg=<level>]
       <command> [<args> ...]"""

cli_options = """Options:
   -v, --version
      Prints the mio version and exits.
   
   -h, --help
      Prints the overall synopsis and a list of the most commonly used commands and exits.
   
   --list-commands
      Prints a list of all mio commands and exits.
      
   -C <path>, --wd=<path>
      Run as if mio was started in <path> instead of the current working directory.  When multiple -C options are
      given, each subsequent non-absolute -C <path> is interpreted relative to the preceding -C <path>.  If <path> is
      present but empty, e.g. -C "", then the current working directory is left unchanged.
   
   -c <name>[=<value>], --config=<name>[=<value>]
      Pass a configuration parameter to the command.  The value given will override values from configuration files.
      The <name> is expected in the same format as listed by `mio config` (subkeys separated by dots).
      
      Note that omitting the `=` in `mio -c foo.bar ...` is allowed and sets `foo.bar` to the boolean true value (just
      like `[foo]bar` would in a config file).  Including the equals but with an empty value (like
      `mio -c foo.bar= ...`) sets foo.bar to the empty string which `mio config --type=bool` will convert to `false`.
      
   --config-env=<name>=<envvar>
      Like `-c <name>=<value>`, give configuration variable <name> a value, where <envvar> is the name of an
      environment variable from which to retrieve the value.  Unlike `-c` there is no shortcut for directly setting the
      value to an empty string, instead the environment variable itself must be set to the empty string.  It is an
      error if the `<envvar>` does not exist in the environment.  `<envvar>` may not contain an equals sign to avoid
      ambiguity with `<name>` containing one.
   
   --html-path
      Prints the path, without trailing slash, where mio's HTML documentation is installed and exits.
   
   --man-path
      Prints the manpath (see `man(1)`) for the man pages for this version of Moore.io and exits.
   
   --info-path
      Prints the path where the Info files documenting this version of mio are installed and exits.
   
   -p, --paginate
      Pipe all output into less (or if set, $PAGER) if standard output is a terminal.
   
   -P, --no-pager
      Do not pipe mio output into a pager.
    
   --dbg=<level>
      Enables debugging and tracing outputs from mio. [default: 0]"""

cli_full_command_list = """Full Command List:
   Help and Shell/Editor Integration
      help           Documentation for all mio commands
      help-search    Searches mio documentation for the terms provided and lists the results by relevance.
      doctor         Runs a set of checks to ensure mio installation has what it needs to operate properly
      completion     Produces outputs for shell/editor tab completion of mio commands and contents
   
   Project and Environment Management
      init           Starts project creation dialog
      config         Reads/writes to/from mio configuration space
      new            Creates new source code via the mio template engine
      vcs            Automates version control system tasks
   
   IP and Credentials Management
      ip             Creates, modify and manage IPs
      org            Manages organizations
      team           Manages teams
      user           Manages users
   
   Automate Moore.io, F&OS and Vendor EDA Tools
      sim            Performs necessary steps to simulate IP
      regr           Runs regression(s) against IP(s)
      lint           Executes hdl linting tool(s) against IP(s)
      synth          Executes logic synthesis tool(s) against IP(s)
      timing         Executes timing analysis tool(s) against IP(s)
      formal         Executes formal logic verification tool(s) against IP(s)
      emul           Launches emulation engine(s) against IP(s)
      hdl-connect    HDL source code port connection/disconnection
      hdl-doc        HDL source code documentation generator
      hdl-refactor   HDL re-factorization engine
      hdl-style      HDL source code style policy enforcer
      
   Manage Results and other EDA Tool Outputs
      results        Manages results from EDA tools
      clean          Manages outputs from tools (other than job results)"""

cli_partial_command_list = """These are common `mio` commands used in various situations:

start a project (see also: mio help tutorial)
   init         Starts project creation dialog
   config       Reads/writes to/from mio configuration space
   ip           Creates, modifies and manages IPs
   new          Creates new source code via the mio template engine
   help         Documentation for all mio commands

run design simulations and manage results
   sim          Performs necessary steps to simulate IP
   regr         Runs regression against IP(s)
   results      Views and manage results from EDA tools

automate EDA tools
   lint         Executes hdl linting tool against IP(s)
   synth        Executes logic synthesis tool against IP(s)
   timing       Executes timing analysis tool against IP(s)
   formal       Executes formal logic verification tool against IP(s)
   
See `mio help <command>` to read about a specific subcommand.
See `mio help mio` for an overview of the system."""

mio_text = f"""{logo}
                                     {cli_title}
                                           I N T E R A C T I V E   D E M O

{cli_usage}

{cli_options}

{cli_full_command_list}"""

########################################################################################################################
# IMPORTS
########################################################################################################################
from docopt import docopt
import logging
from . import clean
from . import completion
from . import config
from . import doctor
from . import emul
from . import formal
from . import hdl_connect
from . import hdl_doc
from . import hdl_style
from . import hdl_refactor
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
from . import ip_access
from . import ip_owner
from . import ip_bugs
from . import ip_ci
from . import ip_copy
from . import ip_dedupe
from . import ip_deprecate
from . import ip_diff
from . import ip_docs
from . import ip_edit
from . import ip_cache
from . import ip_explain
from . import ip_explore
from . import ip_fund
from . import ip_hook
from . import ip_init
from . import ip_install
from . import ip_ls
from . import ip_move
from . import ip_outdated
from . import ip_pack
from . import ip_prune
from . import ip_publish
from . import ip_repo
from . import ip_search
from . import ip_star
from . import ip_stars
from . import ip_shrinkwrap
from . import ip_tag
from . import ip_test
from . import ip_uninstall
from . import ip_unpublish
from . import ip_update
from . import ip_version
from . import ip_view
########################################################################################################################


########################################################################################################################
# FUNCTIONS
########################################################################################################################
def process_ip_args(subcommand):
   if subcommand == 'access':
      print(ip_access.__doc__)
      exit()
   elif subcommand == 'author':
      print(ip_owner.__doc__)
      exit()
   elif subcommand == 'bugs':
      print(ip_bugs.__doc__)
      exit()
   elif subcommand == 'cache':
      print(ip_cache.__doc__)
      exit()
   elif subcommand == 'ci':
      print(ip_ci.__doc__)
      exit()
   elif subcommand == 'copy':
      print(ip_copy.__doc__)
      exit()
   elif subcommand == 'dedupe':
      print(ip_dedupe.__doc__)
      exit()
   elif subcommand == 'deprecate':
      print(ip_deprecate.__doc__)
      exit()
   elif subcommand == 'diff':
      print(ip_diff.__doc__)
      exit()
   elif subcommand == 'docs':
      print(ip_docs.__doc__)
      exit()
   elif subcommand == 'edit':
      print(ip_edit.__doc__)
      exit()
   elif subcommand == 'explain':
      print(ip_explain.__doc__)
      exit()
   elif subcommand == 'explore':
      print(ip_explore.__doc__)
      exit()
   elif subcommand == 'fund':
      print(ip_fund.__doc__)
      exit()
   elif subcommand == 'hook':
      print(ip_hook.__doc__)
      exit()
   elif subcommand == 'init':
      print(ip_init.__doc__)
      exit()
   elif subcommand == 'install':
      print(ip_install.__doc__)
      exit()
   elif subcommand == 'ls':
      print(ip_ls.__doc__)
      exit()
   elif subcommand == 'move':
      print(ip_move.__doc__)
      exit()
   elif subcommand == 'outdated':
      print(ip_outdated.__doc__)
      exit()
   elif subcommand == 'owner':
      print(ip_owner.__doc__)
      exit()
   elif subcommand == 'pack':
      print(ip_pack.__doc__)
      exit()
   elif subcommand == 'prune':
      print(ip_prune.__doc__)
      exit()
   elif subcommand == 'publish':
      print(ip_publish.__doc__)
      exit()
   elif subcommand == 'repo':
      print(ip_repo.__doc__)
      exit()
   elif subcommand == 'search':
      print(ip_search.__doc__)
      exit()
   elif subcommand == 'shrinkwrap':
      print(ip_shrinkwrap.__doc__)
      exit()
   elif subcommand == 'star':
      print(ip_star.__doc__)
      exit()
   elif subcommand == 'stars':
      print(ip_stars.__doc__)
      exit()
   elif subcommand == 'tag':
      print(ip_tag.__doc__)
      exit()
   elif subcommand == 'test':
      print(ip_test.__doc__)
      exit()
   elif subcommand == 'uninstall':
      print(ip_uninstall.__doc__)
      exit()
   elif subcommand == 'update':
      print(ip_update.__doc__)
      exit()
   elif subcommand == 'unpublish':
      print(ip_unpublish.__doc__)
      exit()
   elif subcommand == 'version':
      print(ip_version.__doc__)
      exit()
   elif subcommand == 'view':
      print(ip_view.__doc__)
      exit()
   else:
      exit("No such subcommand for `mio ip`")
########################################################################################################################


########################################################################################################################
# ENTRY POINT
########################################################################################################################
def main(upper_args):
   logging.debug("help - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args)
   logging.debug("help - args: " + str(args))
   
   if args['<command>'] == None:
      print(__doc__)
      exit()
   else:
      command = args['<command>']
      if command == 'mio':
         print(mio_text)
         exit()
      elif command == 'clean':
         print(clean.__doc__)
         exit()
      elif command == 'completion':
         print(completion.__doc__)
         exit()
      elif command == 'config':
         print(config.__doc__)
         exit()
      elif command == 'doctor':
         print(doctor.__doc__)
         exit()
      elif command == 'emul':
         print(emul.__doc__)
         exit()
      elif command == 'formal':
         print(formal.__doc__)
         exit()
      elif command == 'hdl-connect':
         print(hdl_connect.__doc__)
         exit()
      elif command == 'hdl-doc':
         print(hdl_doc.__doc__)
         exit()
      elif command == 'hdl-refactor':
         print(hdl_refactor.__doc__)
         exit()
      elif command == 'hdl-style':
         print(hdl_style.__doc__)
         exit()
      elif command == 'help-search':
         print(help_search.__doc__)
         exit()
      elif command == 'help':
         print(help.__doc__)
         exit()
      elif command == 'init':
         print(init.__doc__)
         exit()
      elif command == 'ip':
         if '<subcommand>' not in args or args['<subcommand>'] == None:
            print(ip.__doc__)
            exit()
         else:
            process_ip_args(args['<subcommand>'])
      elif command == 'lint':
         print(lint.__doc__)
         exit()
      elif command == 'new':
         print(new.__doc__)
         exit()
      elif command == 'org':
         print(org.__doc__)
         exit()
      elif command == 'regr':
         print(regr.__doc__)
         exit()
      elif command == 'results':
         print(results.__doc__)
         exit()
      elif command == 'run-script':
         print(run_script.__doc__)
         exit()
      elif command == 'set-script':
         print(set_script.__doc__)
         exit()
      elif command == 'sim':
         print(sim.__doc__)
         exit()
      elif command == 'synth':
         print(synth.__doc__)
         exit()
      elif command == 'team':
         print(team.__doc__)
         exit()
      elif command == 'timing':
         print(timing.__doc__)
         exit()
      elif command == 'user':
         print(user.__doc__)
         exit()
      elif command == 'vcs':
         print(vcs.__doc__)
         exit()
      else:
         exit(f"Invalid command: '{command}'")
########################################################################################################################
