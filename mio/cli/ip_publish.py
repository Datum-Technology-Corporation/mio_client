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


"""Moore.io IP Publish Command
   Publishes an IP to a registry.

Usage: mio ip publish [@<scope>/]<ip> [options]

Options:
   -t <id>, --tag=<id>
      Registers the published IP with the given tag, such that `mio ip install <name>@<tag>` will install this version.
      By default, `mio ip publish` updates and `mio ip install` installs the latest tag. [default: latest]
   
   -a <level>, --access=<level>
      Tells the registry whether this IP should be published as 'public' or 'restricted'.  If you don't have a paid
      account, you must publish with `--access public` to publish scoped packages.
   
   -o <code>, --otp=<code>
      If you have two-factor authentication enabled, then you can provide a code from your authenticator with this.  If
      you do not include it here, you will be prompted later.
   
   -d, --dry-run
      Does everything publish would do except actually publishing to the registry. Reports the details of what would
      have been published.
  
Examples:
   mio ip publish @my_scope/my_public_ip                          # Publish public IP
   mio ip publish @my_scope/my_secret_ip -a restricted -t stable  # Publish restricted IP with a tag
   mio ip publish -d -o 189273973184                              # Perform a publish dry-run with an inlined OTP code"""


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
   logging.debug("ip_publish - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("ip_publish - args: " + str(args))
########################################################################################################################
