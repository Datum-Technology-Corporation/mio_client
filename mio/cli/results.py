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


"""Moore.io Results Command
   Manages results from EDA tools like a database with actions taken against result files selected via a simple query
   language.  Teams and organizations can capture their retention policies and choose when to execute them via
   `mio config`.  These can also be run manually at any time via `mio results policy <name>`.
   
   The query language, a modified version of YAML Path
   (https://github.com/wwkimball/yamlpath/wiki/Segments-of-a-YAML-Path) is used to select data from the results
   database to be acted upon (the 'action'):
      Ex: `mio results compress all[size >= 50]`    # Compresses all results files from all IPs over 50 Megabytes
          `mio results delete   my_ip.sim[age > 3]` # Deletes sim results older than 3 days for a specific IP
          `mio results view     sim`                # View latest sim results
   
   The following actions are currently available: 'view', 'compress', 'decompress', 'delete', 'pack', 'collate', 'move',
   'copy'.  If no action is specified, 'view' is assumed.
   
   The following job types are currently available: 'all', 'sim', 'simlogs', 'cov', 'waves', 'regr', 'lint', 'formal',
   'emul', 'synth' and 'timing'.  If the job type is not specified, then the last job type run is assumed.  Specifying
   'sim' selects {'simlogs', 'cov', 'waves'}.
   
   By default, the latest result is selected.

Usage:
   mio results policy     [options] [<name>]           Applies results retention policy as specified in Configuration
   mio results [view]     [options] [<query>]          Opens results in $EDITOR or application specific to data type
   mio results compress   [options] [<query>]          Replaces files with tarballs (ex: `a.log -> a.log.tgz`)
   mio results decompress [options] [<query>]          Replaces tarballs with files (ex: `a.log.tgz -> a.log`)
   mio results delete     [options] [<query>]          Deletes results from file system
   mio results collate    [options] [<query>] <label>  Combines results from separate runs (not all types)
   mio results pack       [options] [<query>] <dst>    Creates single tarball(s) (.tgz) from results
   mio results move       [options] [<query>] <dst>    Move results into new file system location
   mio results copy       [options] [<query>] <label>  Copy results under a label for archiving

Options:
   -e <cmd>, --editor=<cmd>  Specify the editor to use for `mio results view`
   -F      , --force         Forces the deletion of files (if read-only and/or locked)
   -d      , --delete-orig   Deletes the original files when packing
  
Examples:
   mio results view                           # View latest results for Default IP
   mio results view my_ip.sim                 # View latest simulation results for a specific IP
   mio results -e vmngr *.regr.cov            # View latest regression coverage results for all Project IPs in `vmngr`
   mio results compress some_ip.simlogs[*]    # Compress all the simulation logs for a specific IP
   mio results decompress @my_scope/my_ip     # Decompress all results for a specific IP
   mio results delete -F *.sim[age>7]         # Forcibly delete simulation results older than a week for all Project IPs
   mio results delete *.waves[>500]           # Delete all waveforms over 500 Megabytes in size
   mio results collate my_ip.cov[age<=.1]     # Merge coverage data of all simulations in the last hour for an IP
   mio results pack *.regr[age<=7] ~/bak.tgz  # Pack all regression results from the last week
   mio results move *.waves[age>1] /fs01/arc  # Move all waves older than a day and symlink them locally
   mio results copy *.synth /fs01/netlists    # Archive all Project IP netlists"""


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
   logging.debug("results - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=True)
   logging.debug("results - args: " + str(args))
########################################################################################################################
