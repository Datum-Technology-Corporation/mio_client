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


"""Moore.io IP Access Command
   Used to set access controls on private IPs. For all of the subcommands,
   `ip access` will perform actions on the IP(s) in the current working
   directory if no IP name is passed to the subcommand.
   
   * `public` / `restricted`: Set an IP to be either publicly accessible or
     restricted.
   * `grant / revoke: Add or remove the ability of users and teams to have
     read-only or read-write access to an IP.
   * `2fa-required` / `2fa-not-required`: Configure whether an IP requires that
     anyone publishing it have two-factor authentication enabled on their
     account.
   * `ls-ip`: Show all of the IPs a user or a team is able to access, along with
     the access level, except for read-only public IPs (it won't print the whole
     registry listing)
   * `ls-collaborators`: Show all of the access privileges for an IP. Will only
     show permissions for IPs to which you have at least read access. If <user>
     is passed in, the list is filtered only to teams that user happens to
     belong to.
   * `edit`: Set the access privileges for an IP using $EDITOR.

Usage:
   mio ip access public                                    [<ip>] [options]
   mio ip access restricted                                [<ip>] [options]
   mio ip access grant <read-only|read-write> <scope:team> [<ip>] [options]
   mio ip access revoke                       <scope:team> [<ip>] [options]
   mio ip access 2fa-required                              [<ip>] [options]
   mio ip access 2fa-not-required                          [<ip>] [options]
   mio ip access edit                                      [<ip>] [options]
   mio ip access ls-collaborators [<ip> [<user>]]                 [options]
   mio ip access ls-ip            [<user>|<scope>|<scope:team>]   [options]

Options:
   -r <url>, --registry=<url>
      Specifies the registry to search for IPs.
   
   -o <code>, --otp=<code>
      If you have two-factor authentication enabled, you will need to include a
      one-time password on the command line
  
Examples:
   mio ip access public my_ip                                   # Make 'my_ip' a public IP
   mio ip access grant  read-write my_team my_ip                # Give read/write access to 'my_team' for 'my_ip'
   mio ip access revoke other_team my_ip                        # Revoke all access to 'other_team' for 'my_ip'
   mio ip access 2fa-required my_ip -r https://my-registry.com  # Require 2-factor authentication for my_ip in a custom registry
   mio ip access edit my_ip                                     # Open access rights for 'my_ip' in $EDITOR
   mio ip access ls-ip aturing                                  # Lists IPs specific user has access to"""


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
   logging.debug("ip_access - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("ip_access - args: " + str(args))
########################################################################################################################
