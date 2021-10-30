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


"""Moore.io IP Deprecate Command
   Updates registry entry for IP.

Usage: mio ip deprecate [@<scope>/]<ip>[@<version range>] [options] <message>

Options:
   -r, --restore   Un-deprecates IP (if was deprecated)
  
Examples:
   mio ip deprecate my_ip@"< 0.2.3" "Critical bug fixed in v0.2.3"
   mio ip deprecate my_other_ip@1.x "1.x is no longer supported"
   mio ip deprecate my_other_ip@1.x --restore "Oups, user error"""


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
   logging.debug("ip_deprecate - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("ip_deprecate - args: " + str(args))
########################################################################################################################
