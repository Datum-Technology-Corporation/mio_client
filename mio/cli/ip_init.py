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


"""Moore.io IP Init Command
   Creates an `ip.yml` file for a new IP.

Usage: mio ip init [<generator>] [@<scope>/][<name>] [options] -- <arguments>
   
   IP Init can accept multiple 'mlist' files. The following is a sample to be used with `--m-file`:
   ```
   % mio@0.3.7
   $ ip init
      @my_scope/my_ip_generator@2.1
      -n my_ip
   --
      ss-full-name='Large System'
      num-ports=12
   ```

Options:
   -n <string>, --name=<string>      Specifies name of new construct
   -s         , --skip               Skips generator questionnaire
   -r <url>   , --registry=<url>     Specifies the registry to which the new IP belongs
   -f <path>  , --m-file=<path>      Specifies mlist from which to load mio and generator arguments.
   -i <path>  , --args=<path>        Specifies arguments (YAML) file (inline arguments take precedence)
   -q         , --quiet              Mutes generator output.
   -p <path>  , --output-dir=<path>  Specifies output path.
   -d         , --dry-run            Only prints commands mio would normally execute.
   -m         , --m-run              Only prints the mlist file contents for the mio command.

Examples:
   mio ip init                                      # Create ip.yml through stock questionnaire
   mio ip init ! -n my_other_ip                     # Re-run last ip init command with different name
   mio ip init -m ./my_ip.mlist                     # Run mlist file with all arguments
   mio ip init my_gen -n my_ip -i ./my_ip_spec.yml  # Init a named IP from a specific generator with args
   mio ip init my-generator -p ./some_path -q       # Use a generator with a custom path and no text output
   mio ip init my_ip -- -a --b=1 -c=2               # Use stock behavior, but answer questions with inline args
   mio ip init ! -m > ./redo.mlist                  # Save last ip init command to disk"""


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
   logging.debug("ip_init - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("ip_init - args: " + str(args))
########################################################################################################################
