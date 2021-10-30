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


"""Moore.io Run Script Command
   Run Project scripts or from IPs.

Usage: mio run-script [[@<scope>/]<ip>] <command> [options] [-- <args>]

Options:
   -i, --if-present               Does not produce error if script is not found.
   -s, --silent                   Mutes script output
   -f <path>, --args-file=<path>  Specifies an argument file (in-line arguments take precedence)

Aliases: run, rum, urn

Examples:
   mio run-script my-command                                  # Run specific Project script with no arguments
   mio run-script @my_scope/my_ip that_command -- -abc --d=2  # Run script from specific IP with inline arguments
   mio run-script this_command -is --args-file=./my_args.txt  # Run Project script silently with arguments from file"""


########################################################################################################################
# IMPORTS
########################################################################################################################
from docopt import docopt
import logging
########################################################################################################################


########################################################################################################################
# FUNCTIONS
########################################################################################################################
########################################################################################################################


########################################################################################################################
# ENTRY POINT
########################################################################################################################
def main(upper_args):
   logging.debug("run_script - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("run_script - args: " + str(args))
########################################################################################################################
