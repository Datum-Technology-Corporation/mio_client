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


"""Moore.io IP Edit Command
   Opens IP source in default editor. If IP is a dependency, it is first imported into the source tree.

Usage:
   mio ip edit [[@<scope>]/<ip> ...] [options]
   mio ip edit *                     [options]

Options:
   -a, --auto-build
      If enabled, IP will be automatically built upon file changes (see configuration field `default-auto-build` for
      more info).
   -e <command>, --editor=<command>
      Forces mio to execute `command <file1> <file2> ...` over $EDITOR.
  
Examples:
   mio ip edit                  # Edit Default IP in default-editor
   mio ip edit some_ip -a       # Edit IP dependency with auto-build enabled
   mio ip edit --editor=xemacs  # Edit Default IP in `xemacs`
   mio ip edit * -e vi          # Edit all IPs in `vi`. Warning: for code ninjas only"""


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
   logging.debug("ip_edit - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("ip_edit - args: " + str(args))
########################################################################################################################
