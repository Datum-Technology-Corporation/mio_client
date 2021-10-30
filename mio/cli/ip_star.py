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


"""Moore.io IP Star Command
   Mark your favorite IPs. "Starring" an IP means that you have some interest in it. It's a positive way to show that
   you care. Boolean only: starring repeatedly has no additional effect.

Usage:
   mio ip star [[@<scope>/]<ip> ...] [options]

Options:
   -r <url> , --registry=<url>  Specifies the registry the IP(s) belong to.
  
Examples:
   mio ip star @my_scope/my_ip                             # Mark an IP as a favorite
   mio ip star some_ip another_ip -r http://registry.com/  # Mark an IPs as favorites from a specific registry"""


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
   logging.debug("ip_star - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("ip_star - args: " + str(args))
########################################################################################################################
