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


"""Moore.io IP Prune Command
   Removes extraneous IPs. If an IP name is provided, then only IPs matching one of the supplied names are removed.
   
   Extraneous IPs are those present in IP dependencies directories that are not listed as any IP's dependency list.

Usage:
   mio ip prune [[@<scope>/]<ip> ...] [options]
   mio ip prune *                     [options]

Options:
   -d, --dry-run  Disables any action(s) from taking place
  
Examples:
   mio ip prune                               # Prune dependency tree for Default IP
   mio ip prune @some_scope/some_ip my_ip -p  # Prune multiple IP trees
   mio ip prune *                             # Prune all IP trees"""


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
   logging.debug("ip_prune - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("ip_prune - args: " + str(args))
########################################################################################################################
