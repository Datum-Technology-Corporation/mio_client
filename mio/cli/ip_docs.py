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


"""Moore.io IP Docs Command
   Opens IP documentation. Use
   `ip config set default-editor-<extension> <editor>` to change the default program in which documentation will be
   viewed.

Usage:
   mio ip docs [[@<scope>]/<ip> ...] [options]
   mio ip docs *                     [options]

Options:
   -f <extension>, --format=<extension>
      Specify documentation format to load/launch: html, pdf or man
      [default: html]
  
Examples:
   mio ip docs                         # Open up html documentation for default IP
   mio ip docs --format=man            # View man help pages for the default IP
   mio ip docs some_ip                 # View documents for IP
   mio ip docs this_ip that_ip -f pdf  # Launch default PDF viewer for 2 IPs
   mio ip docs * --format=html         # Open up documentation for all Project IPs in browser"""


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
   logging.debug("ip_docs - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("ip_docs - args: " + str(args))
########################################################################################################################
