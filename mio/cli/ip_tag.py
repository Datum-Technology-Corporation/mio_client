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


"""Moore.io IP Tag Command
   Adds, removes, or enumerates distribution tags on an IP.

Usage:
   mio ip tag add [@<scope>/]<ip>@<version> [<tag>] [options]  Create new tag for IP and version
   mio ip tag rm  [@<scope>/]<ip>            <tag>  [options]  Remove existing tag
   mio ip tag ls  [@<scope>/]<ip>]                  [options]  List existing tag(s)

Options:
   -o <code>, --otp=<code>
      If you have two-factor authentication enabled, you will need to include a one-time password on the command line
  
Examples:
   mio ip tag add my_ip@1.0.0 stable
   mio ip tag rm  my_ip       beta"""


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
   logging.debug("ip_tag - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("ip_tag - args: " + str(args))
########################################################################################################################
