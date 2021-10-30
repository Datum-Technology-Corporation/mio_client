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


"""Moore.io IP Install Command
   Installs an IP and any IPs that it depends on.  If command is run from within an IP directory, the command will
   append the newly installed IP to the target IP's dependency list.

   * `mio ip install` (in an IP directory, no arguments): installs the dependencies for the local IP into the nearest
     IP imports directory.
   * `mio ip install --directory=<path>`: installs IP from a specified path as a symlink.
   * `mio ip install --tarball=<path>`: installs IP from a tarball (.tar, .tar.gz, .tgz).  If the root of the tarball
     has zero or more than one directory, it will be considered the root of the IP.  If there is only one directory
     present, that sub-directory will be considered the root of the IP.
   * `mio ip install <ip uri>`: installs IP from a registry.
   * `mio ip install alias:<ip uri>`: installs IP from a registry with an aliased name.
   
   An IP URI is either:
      * Latest IP version in a registry: `` (empty string)
      * Tagged IP version in a registry: `[@<scope>/]<name>@<tag>`
           Ex: `@my_scope/my_ip@latest`
      * Specific IP version in a registry: `[@<scope>/]<name>@<major>.<minor>.<patch>`
           Ex: `@my_scope/my_ip@1.0.0`
      * A version range for an IP in a registry: `[@<scope>/]<name>@"<version range>"` (single quotes are also valid)
           Ex: `@my_scope/my_ip@">=0.1.0 <0.2.0"`
               `@my_scope/my_ip@"16 - 17"
      * The latest version of an IP located in a repository: `<protocol>://<hostname>[:<port>]/<path>`
           Ex: `git://github.com/my-org/my-repo.git`
      * The commit-ish for an IP located in a repository: `<protocol>://<hostname>[:<port>]/<path>#<commit-ish>`
           Ex: `git://github.com/my-org/my-repo.git#v1.0.27`
               `git://github.com/my-org/my-repo.git#pull/273`
      * The semver (semantic versioning) for an IP located in a repository:
        `<protocol>://<hostname>[:<port>]/<path>@<semver>`. Protocol is one of `git`, `git+ssh`, `git+http`, `git+https`
         or `git+file`.
           Ex: `git://github.com/my-org/my-repo.git@^5.0`

Usage:
   mio ip install [-g | --global] [-d <path> | --dir=<path>]
   mio ip install [<alias>:][@<scope>/]<name>[@<version>]                                      [options]
   mio ip install [<alias>:][@<scope>/]<name>[@"<version range>"]                              [options]
   mio ip install [<alias>:][@<scope>/]<name>[@'<version range>']                              [options]
   mio ip install [<alias>:]<protocol>://<hostname>[:<port>]/<path>[#<commit-ish> | @<semver>] [options]

Options:
   -g       , --global          Installs IP(s) into global IP store.
   -c       , --clean           Performs clean install (removes all IP dependencies first)
   -d <path>, --dir=<path>      Installs IP from specified path.
   -r <url> , --registry=<url>  Specifies the registry to install IP from.

Examples:
   mio ip install                                                          # Install dependencies for project or local
                                                                           # IP
   mio ip install some_ip@1.0.0                                            # Install a specific version of an IP in the
                                                                           # registry
   mio ip install git://github.com/some-org/some-repo.git@^1.0             # Install approximately version 1.0 of an IP
                                                                           # in a git repository
   mio ip install my_alias:@some_scope/some_ip@stable -r https://reg-url/  # Install a tagged IP version from a specific
                                                                           # registry under a specific name (i.e.
                                                                           # alias)"""


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
   logging.debug("ip_install - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("ip_install - args: " + str(args))
########################################################################################################################
