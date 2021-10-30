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


"""Moore.io Completion Command
   Produces outputs for shell/editor tab completion of mio commands and hdl
   symbols from populated IPs.

Usage:
   mio completion [--mio-commands] [--shell=<variant>]
   mio completion  --ctags         [--variant=<type> ]

Options:
   -m, --mio-commands
      Outputs Moore.io commands completion text
   
   -s <variant>, --shell=<variant>
      Specify shell variant for completion: bash, csh, zsh [default: bash]
   
   -c, --ctags
      Outputs Ctags of IP HDL symbols
   
   -v <type>, --variant=<type>
      Specifies which CTags variant to use: ctags, etags [default: ctags]
  
Examples:
   source <(mio completion --shell=csh)
   mio completion --mio-commands              >> /usr/local/etc/bash_completion.d/mio
   mio completion --mio-commands --shell=bash >> ~/.bashrc
   mio completion --ctags                     >> ~/tags/my_project.tags
"""


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
   logging.debug("completion - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("completion - args: " + str(args))
########################################################################################################################
