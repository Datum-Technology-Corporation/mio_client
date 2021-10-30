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


"""Moore.io Org(anization) Command
   Organization management.

Usage:
  mio org set <orgname>  <username>  [developer | admin | owner] [options]
  mio org rm  <orgname>  <username>                              [options]
  mio org ls  <orgname> [<username>]                             [options]

Options:
   -r <url>, --registry=<url>
      The base URL of the IP registry.
   -o <code>, --otp=<code>
      One-time password from a two-factor authenticator
   -f <type>, --format=<type>
      Specifies output format: text, yml, xml, json, csv [default: text]
   -t, --use-tabs
      Output search results as lines with tab-separated columns.

Examples:
   mio org set my-org @cbabbage       # Add a new developer to an org
   mio org set my-org @aturing admin  # Add a new admin to an org (or change a developer to an admin)
   mio org rm  my-org cbabbage        # Remove a user from an org
   mio org ls  my-org                 # List all users in an org
   mio org ls  my-org -f json         # List all users in JSON format
   mio org ls  my-org @aturing        # See what role a user has in an org"""


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
   logging.debug("org - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("org - args: " + str(args))
########################################################################################################################
