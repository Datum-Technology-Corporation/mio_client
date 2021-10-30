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


"""Moore.io Formal Command
   Executes formal logic verification tool against IP(s).
   
   Formal can accept multiple 'mlist' files. The following is a sample to be used with `--m-file`:
   ```
   % mio@0.3.7
      --config=def=456
      --config-env='username'=USER
   $ formal
      @my_scope/my_ip@2.1.0-rc.2
      --app=jasper@3.1.15
   --
      dp-width=32B
      phy-bypass=yes
   ---
      --ignore-warnings
   ```

Usage:
   mio formal [[@<scope>/]<ip> ...] [options] [-- <params>] [--- <args>]  Runs specific formal job
   mio formal !                     [options] [-- <params>] [--- <args>]  Re-runs last emulation

Options:
   -a <name>, --app=<name>  Specifies formal application name (must be in mio Configuration).
   -g       , --gui         Invokes formal tool in graphical or 'GUI' mode.
   
   -f <path>, --m-file=<path>      Specifies mlist from which to load mio arguments, IP parameters and Tool arguments.
   -x <path>, --tcl-script=<path>  Specifies TCL script to be executed by emulation tool.
   -n <path>, --netlist=<path>     Specifies design netlist to use.
   
   -l <string> , --label=<string>      Specifies results label.  Used as a prefix/suffix in file and/or directory names.
   -q          , --quiet               Mutes formal tool output to stdout.
   -p <path>   , --results-dir=<path>  Specifies results directory path.  A symlink is created in the local results.
   -d          , --dry-run             Only Prints the commands mio would normally execute to perform formal verif.
   -m          , --m-run               Only prints the mlist file contents for the mio command.

Examples:
   # TBD"""


########################################################################################################################
# IMPORTS
########################################################################################################################
from docopt import docopt
import logging
########################################################################################################################


########################################################################################################################
# ENTRY POINT
########################################################################################################################
def main(upper_args):
   logging.debug("formal - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("formal - args: " + str(args))
########################################################################################################################
