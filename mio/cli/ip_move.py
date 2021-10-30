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


"""Moore.io IP Move Command
   Move an IP to a new location or rename it.

Usage:
   mio ip move [[@<scope>/]<ip>[@<version]] [<new name>] [options]

Options:
   -g       , --global              Move IP from global IP directory
   -r <url> , --registry=<url>      Specifies registry from which to move IP
   -d <path>, --destination=<path>  Specifies path to move to (default is to move locally)
  
Examples:
   mio ip move my_new_named_ip                               # Rename Default IP
   mio ip move @my_scope/my_ip --destination=/home/cbabbage  # Move scoped IP out of project
   mio ip move src_ip dst_ip -r https://my-registry.com      # Rename IP in specific Registry"""


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
   logging.debug("ip_move - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("ip_move - args: " + str(args))
########################################################################################################################
