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


"""Moore.io Init Command
   Creates .mio.toml configuration file for a new Project.
   
   Init can accept multiple 'mlist' files. The following is a sample to be used with `--m-file`:
   ```
   % mio@0.3.7
   $ init
      @my_scope/my_proj_generator@2.1.0-rc.2
      -n my_project
   --
      client-name=acme
      encrypt=True
   ```

Usage:
   mio init [<generator>] [options] -- <args>  Creates specific Project
   mio init !             [options] -- <args>  Re-runs last `init` command

Options:
   -n <string>, --name=<string>      Specifies name of new construct
   -s         , --skip               Skips generator questionnaire
   -f <path>  , --m-file=<path>      Specifies mlist from which to load mio and generator arguments.
   -i <path>  , --args=<path>        Specifies arguments (YAML) file (inline arguments take precedence)
   -q         , --quiet              Mutes generator output.
   -p <path>  , --output-dir=<path>  Specifies output path.
   -d         , --dry-run            Only prints commands mio would normally execute.
   -m         , --m-run              Only prints the mlist file contents for the mio command.

Examples:
   mio init                                               # Create Project .mio.toml through stock questionnaire
   mio init ! -n my_other_project                         # Re-run last init command with different name
   mio init -m ./my_project.mlist                         # Run mlist file with all arguments
   mio init my_gen -n my_project -i ./my_proj_spec.yml    # Init a named Project from a specific generator with args
   mio init my-generator -p ./some_path -q                # Use a generator with a custom output path and no text output
   mio init my_project -i=./my_args.yml -- -a --b=1 -c=2  # Use stock behavior, but answer questions with file and args
   mio init ! -m > ./redo.mlist                           # Save last init command to disk"""



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
   logging.debug("init - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=True)
   logging.debug("init - args: " + str(args))
########################################################################################################################
