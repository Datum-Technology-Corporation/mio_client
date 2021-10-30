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


"""Moore.io IP Command
   Attempts to simplify the overall structure by moving dependencies further up
   the tree

Usage: mio ip dedupe [options]

Options:
   -d, --dry-run
      Lists duplicate IPs and the resulting optimized dependency tree, but does
      not perform any actual operations.
   -f <type>, --format=<type>
      Specifies output format: text, yml, xml, csv [default: text]
  
Examples:
   mio ip dedupe -d                  # Print out duplicate IPs only
   mio ip dedupe -f csv > waste.csv  # Print out duplicate dependencies that were moved to csv file"""


########################################################################################################################
# IMPORTS
########################################################################################################################
from docopt import docopt
import logging
########################################################################################################################


########################################################################################################################
# ENTRY POINT
def main(upper_args):
   logging.debug("ip_dedupe - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("ip_dedupe - args: " + str(args))
########################################################################################################################
