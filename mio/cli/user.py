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


"""Moore.io User Command
   Manages User profile.

Usage:
  mio user add                              [options]  Create or verify a user
  mio user login                            [options]  Saves credentials to .mio.toml
  mio user logout                           [options]  Removes credentials and tokens from .mio.toml
  mio user profile get [<property>]         [options]  Displays one or all profile properties
  mio user profile set <property> <value>   [options]  Sets profile property
  mio user profile set password                        Sets profile password
  mio user profile enable-2fa               [options]  Enables two-factor authentication
  mio user profile disable-2fa                         Disables two-factor authentication
  mio user token  (list | create | revoke)  [options]  Manages authentication tokens
  mio user whoami                           [options]  Displays mio user name

Options:
   -r <url> , --registry=<url>  Specifies the URL of the Registry the User belongs to
   -s <name>, --scope=<name>    Specifies the scope the User belongs to
   -a <type>, --auth=<type>     Specifies the type of authentication
   -f <type>, --format=<type>   Specifies input/output format: text, yml, xml, json, csv [default: text]
   -t       , --use-tabs        Outputs results as lines with tab-separated columns.
   -R       , --read-only       Marks a token as unable to publish
   -o <code>, --otp=<code>      Specifies two-factor authentication code

Examples:
   mio user add                                                     # Add new user to default Registry
   mio user login -o 123123 -s my_scope -r https://my-registry.com  # Log in using otp code to specific scope
   mio user profile get email                                       # Print user email address
   mio user profile set last-name Babbage                           # Set user property
   mio user profile get -f xml                                      # Print entire user profile in XML format
   mio user profile enable-2fa -a sqrl                              # Enable two-factor authentication using SQRL
   mio user token list --format=yml                                 # Print out all user tokens in YAML format
   mio user token create -R                                         # Create read-only token for user
   mio user whoami                                                  # Print user name for default Registry"""


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
   logging.debug("user - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("user - args: " + str(args))
########################################################################################################################
