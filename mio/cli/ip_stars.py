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


"""Moore.io IP Stars Command
   View IPs marked as favorites.

Usage:
   mio ip stars [<user>] [options]

Options:
   -r <url> , --registry=<url>  Specifies the registry the user belongs to.
   -f <type>, --format=<type>   Specifies output format: text, yml, xml, json, csv [default: text]
  
Examples:
   mio ip stars                                  # View your favorite IP(s)
   mio ip stars aturing -r http://registry.com/  # View favorite IP(s) of a specific user from a specific registry"""


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
   logging.debug("ip_stars - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("ip_stars - args: " + str(args))
########################################################################################################################
