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


"""Moore.io IP Cache Command
   Used to add, list, or clean the mio IP cache folder:
   * `update`: Add the specified IPs to the local cache. This command is primarily
     intended to be used internally by mio, but it can provide a way to add data
     to the local installation cache explicitly.
   * `clean`: Delete all data out of the cache folder. Note that this is
     typically unnecessary, as mio's cache is auto-managed.
   * `verify`: Verify the contents of the cache folder, garbage collecting any
     unneeded data, and verifying the integrity of the cache index and all
     cached data.

Usage:
mio ip cache update [--force]
mio ip cache clean
mio ip cache verify

Options:
   -f, --force   Performs clean before updating the cache"""


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
   logging.debug("ip_cache - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("ip_cache - args: " + str(args))
########################################################################################################################
