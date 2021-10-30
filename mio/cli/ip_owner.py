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


"""Moore.io IP Owner Command
   Manage ownership of published IPs.
   
   * `ls` : List all the users who have access to modify an IP and push new versions. Handy when you need to know who
            to bug for help.
   * `add`: Add a new user as a maintainer of an IP. This user is enabled to modify metadata, publish new versions, and
            add other owners.
   * `rm` : Remove a user from the IP owner list. This immediately revokes their privileges.
   
   Note that there is only one level of access. Either you can modify an IP, or you can't. Future versions may contain
   more fine-grained access levels, but that is not implemented at this time.

   If you have two-factor authentication enabled with auth-and-writes (see mio-profile) then you'll need to include an
   otp on the command line when changing ownership with --otp.

Usage:
   mio ip owner add <user> [@<scope>/]<ip> [options]  Adds owner to target IP
   mio ip owner rm  <user> [@<scope>/]<ip> [options]  Removes owner from target IP
   mio ip owner ls         [@<scope>/]<ip> [options]  Lists owners for target IP

Options:
   -o <code>, --otp=<code>  Specifies two-factor authentication code

Examples:
   mio ip owner add alovelace my_ip  # Add new owner to IP
   mio ip owner rm  jclement  my_ip  # Remove owner from IP
   mio ip owner ls            my_ip  # List owners for IP"""


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
   logging.debug("ip_owner - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("ip_owner - args: " + str(args))
########################################################################################################################
