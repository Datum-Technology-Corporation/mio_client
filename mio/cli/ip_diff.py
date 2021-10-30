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


"""Moore.io IP Diff Command
   Prints diff patches of files for IPs published to the mio registry.
   
   Allows for IPs to be specified either via:
      * Semver: see 'https://semver.org' to learn more
      * Registry Specifier: `[https://<registry base url>/][@<scope>/]<ip>[@<version>]`

Usage:
   mio ip diff version <semver-b>            [options]  Compares Default IP against version specified with semver
   mio ip diff version <semver-a> <semver-b> [options]  Compares two Default IP versions specified with semver
   mio ip diff spec    <spec-b>              [options]  Compares Default IP against version specified by specifier
   mio ip diff spec    <spec-a>   <spec-b>   [options]  Compares two IP versions using specifiers

Options:
   -g, --global            Looks for IPs in global directory
   -i, --ignore-all-space  Ignores whitespace when comparing lines
   -n, --name-only         Only prints filenames

Examples:
   mio ip diff version stable                                            # Diff Default IP against tag
   mio ip diff version latest  "1.2"                                     # Diff a tag against a specific version of the Default IP
   mio ip diff spec @my_scope/my_ip@latest @my-cope/my_ip_branch@latest  # Diff the latest version of an IP against its branch"""


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
   logging.debug("ip_diff - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("ip_diff - args: " + str(args))
########################################################################################################################
