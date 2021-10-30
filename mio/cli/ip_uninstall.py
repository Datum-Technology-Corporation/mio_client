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


"""Moore.io IP Uninstall Command
   Uninstalls IP(s), completely removing everything mio installed on its behalf.  It also removes the IP(s) from the
   dependencies in ip.yml.  If ip.lock.yml and/or ip.shrinkwrap.yml are present, they are updated as well.

Usage: npm uninstall [<@scope>/]<pkg>[@<version>] ... [options]

Options:
   -g, --global   Uninstalls IPs within the global directory
   -F, --force    Forces updating IP metadata (going against any configuration)
   -n, --no-save  Disables updating ip.yml, ip.lock,yml and/or ip.shrinkwrap.yml

Aliases:  remove, rm

Examples:
   mio ip uninstall @my_scope/my_ip  # Uninstall single IP
   mio ip uninstall a_ip b_ip -gn    # Removes installed IP files in the global directory, but does not update IP metadata"""


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
   logging.debug("ip_uninstall - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("ip_uninstall - args: " + str(args))
########################################################################################################################
