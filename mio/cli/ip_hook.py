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


"""Moore.io IP Hook Command
   Allows you to manage IP hooks, including adding, removing, listing, and updating.  Hooks allow you to configure URL
   endpoints that will be notified whenever a change happens to any of the supported entity types.  Three different
   types of entities can be watched by hooks: IPs, Owners, and Scopes.
   
   * To create an IP hook, simply reference the IP name.
   * To create an owner hook, prefix the owner name with ~ (as in, `~youruser` ).
   * To create a scope hook, prefix the scope name with  @ (as in, `@yourscope`).

   The hook id used by `update` and `rm` are the IDs listed in `mio ip hook ls`
   for that particular hook.

   The shared secret will be sent along to the URL endpoint so you can verify
   the request came from your own configured hook.

Usage:
   mio ip hook ls    [<ip>]
   mio ip hook add <entity> <url>  <secret>
   mio ip hook update <id>  <url> [<secret>]
   mio ip hook rm     <id>
   
Examples:
   mip ip hook add my_ip  https://example.com/ my-shared-secret     # Add a hook to watch an IP for changes
   mip ip hook add ~aturing https://example.com/ my-shared-secret   # Add a hook to watch IPs belonging to specific user
   mip ip hook add @my_scope https://example.com/ my-shared-secret  # Add a hook to watch IPs in a specific scope
   mip ip hook ls                                                   # List all your active hooks
   mip ip hook ls my_ip                                             # List your active hooks for specific IP
   mip ip hook update id-deadbeef https://my-new-website.here/      # Update an existing hook's url
   mip ip hook rm     id-deadbeef                                   # Remove a hook"""


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
   logging.debug("ip_hook - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("ip_hook - args: " + str(args))
########################################################################################################################
