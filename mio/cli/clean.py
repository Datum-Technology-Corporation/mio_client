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


"""Moore.io Clean Command
   Manages output artifacts from all tools (other than job results)

Usage:
   mio clean [[@<scope>]/<ip> ...] [options]   Deletes artifacts for specified IP(s)
   mio clean *                     [options]   Deletes artifacts for all IPs
   
Options:
   -F, --force   Forces the deletion of files (if read-only and/or locked)
   -A, --all     Deletes all EDA tool artifacts
   -s, --sim     Deletes simulation artifacts
   -l, --lint    Deletes linting artifacts
   -f, --formal  Deletes formal verification artifacts
   -y, --synth   Deletes logic synthesis verification artifacts
   -e, --emul    Deletes emulation artifacts
   -t, --timing  Deletes timing analysis artifacts
   
Examples:
   mio clean                                  # Deletes latest artifacts for Default IP
   mio clean --all                            # Deletes all artifacts for Default IP
   mio clean my_ip my_other_ip --sim --lint   # Deletes sim and lint artifacts for 2 IPs
   mio clean * --force -slf                   # Delete sim, lint and formal artifacts for all IPs (with force)
   mio clean * --all                          # Delete all artifacts for all IPs
   mio clean * -AF                            # Delete all artifacts for all IPs, overriding all access rights!"""


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
    logging.debug("clean - upper_args: " + str(upper_args))
    args = docopt(__doc__, argv=upper_args, options_first=False)
    logging.debug("clean - args: " + str(args))
########################################################################################################################
