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


"""Moore.io Timing Command
   Launches Timing Analysis tool against target IP(s).
   
   Timing can accept multiple 'mlist' files. The following is a sample to be used with `--m-file`:
   ```
   % mio@0.4.1
      --config=gh=3
      --dbg=1
   $ timing
      @my_scope/my_ip@2.1.0-rc.2
      --app=cobalt@3.1.15
   --
      dp-width=32B
      phy-bypass=yes
   ---
      --ignore-warnings
   ```

Usage:
   mio timing [[@<scope>/]<ip>[@<version>] ...] [options] [-- <parameters>] [--- <args>]  Runs specific timing job
   mio timing !                                 [options] [-- <parameters>] [--- <args>]  Re-runs last timing run

Options:
   -a <name>, --app=<name>  Specifies timing analysis application name (must be in mio Configuration).
   -g       , --gui         Invokes timing analysis tool in graphical or 'GUI' mode.
   
   -f <path>, --m-file=<path>      Specifies mlist from which to load mio arguments, IP parameters and Tool arguments.
   -x <path>, --tcl-script=<path>  Specifies TCL script to be executed by timing analysis tool.
   -n <path>, --netlist=<path>     Specifies design netlist to use.
   -i <path>, --pdk=<path>         Specifies process PDK to use.
   
   -l <string> , --label=<string>      Specifies results label.  Used as a prefix/suffix in file and/or directory names.
   -q          , --quiet               Mutes timing analysis tool output to stdout.
   -p <path>   , --results-dir=<path>  Specifies results directory path.  A symlink is created in the local results.
   -d          , --dry-run             Only Prints the commands mio would normally execute to perform timing analysis.
   -m          , --m-run               Only prints the mlist file contents for the mio command.
  
Examples:
   # TBD
"""


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
   logging.debug("sta - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("sta - args: " + str(args))
########################################################################################################################
