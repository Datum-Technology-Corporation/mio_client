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


"""Moore.io IP Unpublish Command
   Remove an IP from the registry.  It is recommended to use `mio ip deprecate` if the intent is to encourage users to
   upgrade, or if you no longer want to maintain an IP.

Usage:
   mio ip unpublish [@<scope>/]<ip>@<version>      [options]  Unpublishes a single version of an IP
   mio ip unpublish [@<scope>/]<ip> [-F | --force] [options]  Unpublishes an entire IP

Options:
   -d, --dry-run
      Indicates that you don't want mio to make any changes and that it should only report what it would have done.
   
   -F, --force
      Unpublish and entire IP. Will be prompted for confirmation.

Examples:
   mio ip unpublish @my_scope/my_ip@1.0.0           # Unpublish specific version of an IP
   mio ip unpublish @my_scope/my_doomed_ip --force  # Unpublish entire IP"""


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
   logging.debug("ip_unpublish - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("ip_unpublish - args: " + str(args))
########################################################################################################################
