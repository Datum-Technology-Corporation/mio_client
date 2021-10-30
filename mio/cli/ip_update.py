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


"""Moore.io IP Update Command
   Updates all the IPs listed to the latest version (specified by the tag config), respecting semver.  It will also
   install missing IPs.

Usage:
   mio ip update [options] [[@<scope>]/<ip> ...]
   mio ip update [options] *

Options:
   -g, --global   Installs IP(s) in the global directory
   -f, --fund     Displays number of dependencies looking for funding at the end of installation
   -d, --dry-run  Only reports what changes would have been made
  
Examples:
   mio ip update                        # Update default IP locally
   mio ip update my_ip this_ip that_ip  # Update all dependencies for 3 IPs locally
   mio ip update -gfd *                 # Perform dry run of updating all IPs in project to global IP directory"""


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
   logging.debug("ip_update - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=True)
   logging.debug("ip_update - args: " + str(args))
########################################################################################################################
