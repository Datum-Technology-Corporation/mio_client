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


"""Moore.io IP Ls Command
   Prints all the versions of IPs that are installed, as well as their dependencies when --all is specified, in a tree
   structure.

Usage:
   mio ip ls [[@<scope>/]<ip> ...] [options]
   mio ip ls *                     [options]

Options:
   -a, --all
      Prints dependencies
   
   -g, --global
      Operates in "global" mode, so that
   
   -f <type>, --format=<type>
      Specifies output format: text, yml, xml, json, csv [default: text]
      
   -l, --long
      Displays full IP descriptions and other long text across multiple lines.  When disabled (which is the default)
      the output will truncate search results to fit neatly on a single line.  IPs with extremely long names will fall
      on multiple lines.
      
   -t, --use-tabs
      Output search results as lines with tab-separated columns.
   
   -d <level>, --depth=<level>
      Recursive depth for printing out IPs.  [default: infinity]
   
Examples:
   mio ip ls -a          # Print Default IP dependencies
   mio ip ls this_ip -a  # Print IP info and all its dependencies
   mio ip ls * --all     # Print all IPs and their dependencies"""


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
   logging.debug("ip_list - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("ip_list - args: " + str(args))
########################################################################################################################
