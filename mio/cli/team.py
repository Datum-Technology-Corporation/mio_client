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


"""Moore.io Team Command
   Manage organization teams and team memberships.
   
   Used to manage teams in organizations, and change team memberships. Does not handle permissions for IPs.  Teams must
   always be fully qualified with the organization/scope they belong to when operating on them, separated by a colon
   (:).  That is, if you have a `newteam` team in an `org` organization, you must always refer to that team as
   `@org:newteam` in these commands.

   If you have two-factor authentication enabled in auth-and-writes mode, then you can provide a code from your
   authenticator with [--otp=<otpcode>].  If you don't include this then you will be prompted.

Usage:
  mio team create  @<org>:<team>        [options]
  mio team destroy @<org>:<team>        [options]
  mio team add     @<org>:<team> <user> [options]
  mio team rm      @<org>:<team> <user> [options]
  mio team ls      @<org> | @<org:team> [options]

Options:
   -r <url>, --registry=<url>  Specifies the registry to search for IPs.
   -t       , --use-tabs       Output search results as lines with tab-separated columns.
   -f <type>, --format=<type>  Specifies output format: text, yml, xml, json, csv [default: text]
   -o <code>, --otp=<code>     Specifies two-factor authentication code
  
Examples:
   mio team create  @org:newteam                            # Create a new team under an org
   mio team destroy @org:myteam -o 123                      # Destroy existing team with inline otp code
   mio team add @org:myteam   cbabbage -r https://reg.com/  # Add user to team in specific registry
   mio team rm  @org:thisteam aturing                       # Remove user from team in Default Registry
   mio team ls  @org                                        # List all users in an org
   mio team ls  @org:myteam                                 # List all users in a specific team"""


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
   logging.debug("team - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("team - args: " + str(args))
########################################################################################################################
