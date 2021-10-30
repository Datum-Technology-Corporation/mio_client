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


"""Moore.io Regr(ession) Command
   Executes regression(s) against target IP(s).
   
   Regr can accept multiple 'mlist' files. The following is a sample to be used with `--m-file`:
   ```
   % mio@0.3.7
      --config=def=456
      --config-env='username'=USER
   $ regr
      @my_scope/my_ip@2.1.0-rc.2
      nightly
      nightly-client1
      nightly-client2
   --
      dp-width=64B
   ---
      --hotfix32
   ```

Usage:
   mio regr [[@<scope>/]<ip>] <regression> ... [options] [-- <params>] [--- <args>]  Runs regression(s) against IP
   mio regr [@<scope>/]<ip>/<regression>   ... [options] [-- <params>] [--- <args>]  Runs regression(s) against IP(s)
   mio regr !                                  [options] [-- <params>] [--- <args>]  Re-runs last regr command

Options:
   -f <path>   , --m-file=<path>       Specifies mlist from which to load mio, tool arguments and IP parameters
   -e <address>, --email=<address>     Specifies email address(es) (comma separated) to contact with regression results.
   -l <string> , --label=<string>      Specifies results label.  Used as a prefix/suffix in file and/or directory names.
   -q          , --quiet               Mutes timing analysis tool output to stdout.
   -p <path>   , --results-dir=<path>  Specifies results directory path.  A symlink is created in the local results.
   -d          , --dry-run             Only Prints the commands mio would normally execute to perform timing analysis.
   -m          , --m-run               Only prints the mlist file contents for the mio command.
   
Examples:
   mio regr sanity                               # Run specific regression against Default IP
   mio regr ! -q -- dp-width=64B                 # Re-run last regression with additional parameters and no output
   mio regr -f sanity_mod.mlist -f b34.mlist     # Run two regressions from mlists in parallel
   mio regr @my_scope/my_ip nightly              # Run specific regression against specific IP
   mio regr nightly -f P2.mlist -- multiplier=1  # Run specific regression against specific IP with mixed parameters
   mio regr client_1_bugs client_2_features      # Launch multiple regressions in parallel against Default IP
   mio regr my_ip/sanity some_ip/nightly         # Launch multiple regressions in parallel against multiple IPs
   mio regr ! -m > ./my_regr.mlist               # Save last regression command to disk"""


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
   logging.debug("regr - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("regr - args: " + str(args))
########################################################################################################################
