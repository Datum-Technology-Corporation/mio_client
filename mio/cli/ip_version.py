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


"""Moore.io IP Version Command
   Moves IP to new version.

Usage:
   mio ip version                                                            [options]
   mio ip version <newversion>                                               [options]
   mio ip version (   major |    minor |    patch)                           [options]
   mio ip version (premajor | preminor | prepatch)                           [options]
   mio ip version prerelease [-p <prerelease-id> | --preid=<prerelease-id>]  [options]

Options:
   -f, --allow-same-version
      Prevents throwing an error when the new version has the same value as the current version.
   
   -p <prerelease-id>, --preid=<prerelease-id>
      The "prerelease identifier" to use as a prefix for the "prerelease" part of a semver. Like the rc in `1.2.0-rc.8`.
  
Examples:
   mio ip version                  # Increment 'major' by 1
   mio ip version "1.0.0" -f       # Set version to 1.0.0, overwriting any previous version
   mio ip version patch            # Increment 'patch' by 1
   mio ip version prerelease -p 2  # Set prerelease version to '2' ('x.x.x-rc.2')"""


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
   logging.debug("ip_version - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("ip_version - args: " + str(args))
########################################################################################################################
