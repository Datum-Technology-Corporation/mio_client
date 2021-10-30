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


"""Moore.io Config Command
   Reads/writes to/from mio configuration space.  Moore.io gets it configuration settings from the command line,
   environment variables, `.mio.toml` files, and in some cases, `ip.yml` file(s).
   
   Adding `-c <name>[=<value>] | --config=<name>[=<value>]` and/or `--config-env=<name>=<envvar>` to your CLI command
   (`mio <config-args> <command>`) will add to the Configuration space with the highest level of precedence.
   
   Environment variables prefixed with `MIO_CONFIG_` (case insensitive) will be interpreted as mio Configuration
   parameters.  Any environment variables not given a value will be presumed ass boolean, and given the value `true`.
   
   The remaining order goes as follows (in descending order of importance):
      * Per-project configuration file (`/path/to/my/project/.mio.toml`)
      * Per-user configuration file (defaults to `$HOME/.mio.toml`; configurable via CLI option `--userconfig` or
        environment variable `$MIO_CONFIG_USERCONFIG`)
      * Global configuration file (defaults to `$PREFIX/etc/.mio.toml`; configurable via CLI option `--globalconfig` or
        environment variable `$MIO_CONFIG_GLOBALCONFIG`)
      * Built-in configuration file (`/path/to/mio/.mio.toml`)
      * Internal defaults (`mio config list -i`)
   
   For a full list of Configuration parameters, see
   'https://github.com/Datum-Technology-Corporation/mio_platform_client_cli_mvp/wiki/Configuration-List'.
   
Usage:
   mio config set    [options] <key>=<value> ...  Writes configuration key/value pair(s)
   mio config get    [options] <key>         ...  Prints configuration key(s)
   mio config delete [options] <key>         ...  Deletes key(s)
   mio config list   [options]                    Prints all keys and their values
   mio config edit   [options]                    Open .mio.toml configuration file in editor

Options:
   -p       , --project        Edits the project configuration file
   -u       , --user           Edits the user configuration file
   -g       , --global         Edits the global configuration file
   -i       , --internal       Gets/Lists internal default Configuration
   -e <cmd> , --editor=<cmd>   Override default editor (`$EDITOR`)
   -f <type>, --format=<type>  Specifies output format: text, yml, xml, json, csv [default: text]
  
Examples:
   mio config set default-ip=my_ip -p   # Set Default IP
   mio config set default-test=my_test  # Set Default Test
   mio config get default-simulator     # Print Default Simulator to stdout"""


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
   logging.debug("config - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=True)
   logging.debug("config - args: " + str(args))
########################################################################################################################
