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


"""Moore.io HDL Doc Command
   Generates reference documentation for HDL source code.

Usage:
   mio hdl-doc [[@<scope>]/<ip> ...] [options]
   mio hdl-doc *          [options]

Options:
   -o <path>, --output=<path>   Output files to alternate location
   -a, --all                    Produces all outputs
   -h, --html                   Produces HTML output
   -p, --pdf                    Produces PDF output
   -m, --man                    Produces man page output

Examples:
   mio hdl-doc my_ip my_other_ip -hp   # Generates HTML & PDF documentation for 2 IPs
   mio hdl-doc * -a -o ~/my-ref-doc    # Generates documentation in all formats for all IPs to home directory"""


########################################################################################################################
# IMPORTS
########################################################################################################################
from docopt import docopt
import logging
########################################################################################################################


########################################################################################################################
# FUNCTIONS
########################################################################################################################
def do_hdl_doc(args):
   logging.debug("hdl_doc.do_hdl_doc() - args: " + str(args))
########################################################################################################################


########################################################################################################################
# ENTRY POINT
########################################################################################################################
def main(upper_args):
   logging.debug("hdl_doc.main() - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("hdl_doc.main() - args: " + str(args))
   do_hdl_doc(args)
########################################################################################################################
