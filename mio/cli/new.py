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


"""Moore.io New Command
   Invokes the mio code generator system.  If no generator name is specified, the user is prompted to select from a
   list of what is currently installed (and applicable in this context).  All arguments right of '--' are passed
   untouched to the generator.
   
   New can accept multiple 'mlist' files. The following is a sample to be used with `--m-file`:
   ```
   % mio@0.3.7
   $ new
      @my_scope/my_generator@2.1.0-rc.2
      -n my_instance
   --
      dp-width=64B
      encrypt=True
      phy-present=False
   ```

Usage:
   mio new [[@<scope>/]<ip>] [[@<scope>/]<generator>] [options] [-- <args>]  Runs specific generator
   mio new !                                          [options] [-- <args>]  Re-runs last `new` command

Options:
   -n <string>, --name=<string>      Specifies name of new construct
   -s         , --skip               Skips generator questionnaire
   -f <path>  , --m-file=<path>      Specifies mlist from which to load mio and generator arguments.
   -i <path>  , --args=<path>        Specifies arguments (YAML) file (inline arguments take precedence)
   -q         , --quiet              Mutes generator output.
   -p <path>  , --output-dir=<path>  Specifies output path.
   -d         , --dry-run            Only prints commands mio would normally execute.
   -m         , --m-run              Only prints the mlist file contents for the mio command.

Examples:
   mio new uvm-test --name=smoke                      # Create new UVM test for Default IP named 'smoke'
   mio new ! -s     --name=my_ip                      # Re-run last `new` command with different name with no questions
   mio new uvm-agent -i ./agent-spec.yml -q           # Execute specific generator with arguments file
   mio new @my_scope/my_ip reg-block -f ./spec.mlist  # Create new Register Block for specific IP with an mlist
   mio new some_ip reg -- name=abc size=4B            # Create new Register for a specific IP with inline arguments
   mio new ! -m > ~/template_macro.mlist              # Create mlist file to re-run last new command"""


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
   logging.debug("new - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("new - args: " + str(args))
########################################################################################################################
