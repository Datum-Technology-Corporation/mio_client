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


"""Moore.io IP Pack Command
   Creates tarball (.tgz) of IP(s) and dependencies

Usage:
   mio ip pack [[@<scope>/]<pkg> ...] [options]
   mio ip pack *                      [options]

Options:
   -d, --dry-run
      Does everything that pack usually does without actually packing anything.  That is, report on what would have
      gone into the tarball, but nothing more.
  
Examples:
   mio ip pack my_ip             # Pack single IP
   mio ip pack my_ip some_ip -d  # Pack multiple IPs in a dry-run
   mio ip pack *                 # Pack all IPs"""


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
   logging.debug("ip_pack - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("ip_pack - args: " + str(args))
########################################################################################################################
