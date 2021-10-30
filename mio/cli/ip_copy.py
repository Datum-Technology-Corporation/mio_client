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


"""Moore.io IP Copy Command
   Copy (aka clone) an IP to a new location under a new name.

Usage:
   mio ip copy [[@<scope>/]<ip>[@<version]] <new name> [options]

Options:
   -g       , --global              Copy IP from global IP directory
   -r <url> , --registry=<url>      Specifies registry from which to copy IP
   -d <path>, --destination=<path>  Specifies path to copy to (default is to copy locally)
  
Examples:
   mio ip copy cloned_ip                                       # Copy Default IP locally
   mio ip copy @my_scope/my_ip my_cloned_ip -d /home/cbabbage  # Copy scoped IP to specific directory
   mio ip copy src_ip dst_ip -g -r https://my-registry.com     # Copy IPs globally from specific Registry"""


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
   logging.debug("ip_copy - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("ip_copy - args: " + str(args))
########################################################################################################################
