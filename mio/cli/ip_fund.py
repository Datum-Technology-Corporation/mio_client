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


"""Moore.io IP Fund Command
   Retrieves information on how to fund the Project dependencies. If no IP name is provided, it will list all
   dependencies that are looking for funding in a tree structure, listing the type of funding and the url to visit. If
   IPs are provided, then it tries to open each funding url using the --browser config param; if there are multiple
   funding sources for the IP, each will be opened.

Usage: mio ip fund [[@<scope>]/<ip> ...]
  
Examples:
   mio ip fund                  # Open all Project IPs with funding information
   mio ip fund my_favorite_ip   # Open funding information (if present) for a specific IP"""


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
   logging.debug("ip_fund - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("ip_fund - args: " + str(args))
########################################################################################################################
