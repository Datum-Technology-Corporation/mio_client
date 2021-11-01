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


"""Moore.io VCS Command
   Automates version control system tasks

Usage:
  TBD

Options:
   TBD
  
Examples:
   TBD
"""


########################################################################################################################
# IMPORTS
########################################################################################################################
from docopt import docopt
import logging
########################################################################################################################


########################################################################################################################
# FUNCTIONS
########################################################################################################################
def parse_args(args):
   print(str(args))
########################################################################################################################


########################################################################################################################
# ENTRY POINT
########################################################################################################################
def main(upper_args):
   logging.debug("vcs - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("vcs - args: " + str(args))
   parse_args(args)
########################################################################################################################