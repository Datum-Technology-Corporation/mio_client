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


"""Moore.io IP Search Command
   Search the registry for IPs matching the search terms.  `mio ip search` performs a linear, incremental,
   lexically-ordered search through IP metadata for all files in the registry.  If your terminal has color support, it
   will further highlight the matches in the results.  This can be disabled with the config item `color`.
   
   Search also allows targeting of maintainers in search results, by prefixing their mio username with `=`.

   If a term starts with `/`, then it's interpreted as a regular expression and supports standard GNU RegExp syntax.
   In this case search will ignore a trailing `/` .  (Note you must escape or quote many regular expression characters
   in most shells.)
   
   The mio ip cli caches search results with the same terms and options locally in its cache.  See `mio ip cache` for
   more on how the cache works.

   `prefer-online`
   Forces staleness checks for cached searches, making the cli look for updates immediately even for fresh search
   results.

   `prefer-offline`
   Bypasses staleness checks for cached searches.  Missing data will still be requested from the server.  To force full
   offline mode, use offline.

   `offline`
   Forces full offline mode. Any searches not locally cached will result in an error.

Usage: mio ip search [options] <search term> ...

Options:
   -r <url>, --registry=<url>
      Specifies the registry to search for IPs.
   
   -o <options>, --opts=<options>
      Space-separated options that are always passed to search.
      
   -e <exclusions>, --exclude=<exclusions>
      Space-separated options that limit the results from search.
      
   -f <type>, --format=<type>
      Specifies output format: text, yml, xml, json, csv [default: text]
      
   -l, --long
      Displays full IP descriptions and other long text across multiple lines.  When disabled (which is the default) the
      output will truncate search results to fit neatly on a single line.  IPs with extremely long names will fall on
      multiple lines.
      
   -t, --use-tabs
      Output search results as lines with tab-separated columns.
   
   -n, --no-description
      Omit IP description in the search results.

Examples:
   mio ip search '/my*_ip*/'
   mio ip search --long -e 'exclusion1 exclusion2 ' '/*some*ip*/'
   mip ip search --format=xml '=cbabbage'"""


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
   logging.debug("ip_search - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=True)
   logging.debug("ip_search - args: " + str(args))
########################################################################################################################
