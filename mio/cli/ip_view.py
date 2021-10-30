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


"""Moore.io IP View Command
   Views IP registry information.
   
   If only a single string field for a single version is output, then it will not be colorized or quoted, to enable
   piping the output to another command. If the field is an object, it will be output as a YAML object literal.

   If the --format=<type> flag is given, the outputted fields will be formatted accordingly.

   If the version range matches multiple versions then each printed value will be prefixed with the version it applies
   to.

   If multiple fields are requested, then each of them is prefixed with the field name.

Usage: mio ip view [<@scope>/]<name>[@<version>] [<field>[.<subfield>] ...] [options]

Options:
   -f <type>, --format=<type>   Specifies output format: text, yml, xml, json, csv [default: text]
   -r <url> , --registry=<url>  Specifies the registry to view IP from.
  
Examples:
   mio ip view my_ip                                                # View metadata about 'my_ip'
   mio ip view some_ip@0.3.5 dependencies                           # View dependencies for 'some_ip'
   mio ip view my_ip repository.url                                 # View repository URL for 'my_ip'
   mio ip view that_ip@$(mio ip view this_ip dependencies.that_ip)  # View metadata about the version of 'that_ip' on which 'this_ip' depends
   mio ip view my_ip contributors.email                             # View all email addresses for contributors of 'my_ip'
   mio ip view my_ip contributors[0].email                          # View the email address for the first contributor of 'my_ip'
   mio ip view my_ip contributors.name contributors.email           # View all names and email addresses of the contributors of 'my_ip'
   mio ip view some_ip@'>0.5.4' dependencies.some_other_ip          # View metadata about dependency 'some_other_ip' for all versions of some_ip > 0.5.4
   mio ip view connect my_ip                                        # View version history for 'my_ip'"""


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
   logging.debug("ip_view - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=True)
   logging.debug("ip_view - args: " + str(args))
########################################################################################################################
