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


"""Moore.io IP Command
   IP Management. The following subcommands are available (see
   `mio help ip <subcommand>` for more information):

      View IP metadata
         bugs  ci  docs  explain  fund  ls  outdated  repo  search  stars  view
   
      Operate on the IP registry
         cache  publish  test  unpublish
   
      Modify IP metadata
         access  copy  deprecate  hook  init  integrate  move  owner  shrinkwrap  star  tag  version
   
      Operate on IP dependencies
         dedupe  install  prune  uninstall  update
   
      Operate on IP contents
         diff  edit  exec  explore  pack

Usage: mio ip <command> [<args> ...]"""


########################################################################################################################
# IMPORTS
########################################################################################################################
from docopt import docopt
import sys
from . import ip_access
from . import ip_bugs
from . import ip_cache
from . import ip_ci      # Sends you to IP CI page (Jenkins, Bamboo, etc.) rather than doing a clean install (as in npm); for that, check out `ip update --clean`
from . import ip_copy    # Copies IP
from . import ip_dedupe
from . import ip_deprecate
from . import ip_diff
from . import ip_docs
from . import ip_edit
from . import ip_explain
from . import ip_explore
from . import ip_fund
from . import ip_hook
from . import ip_init   # Creates ip.yml, same as `npm init`, recommended that users use `mio new` (which itself calls `ip init`)
from . import ip_install
from . import ip_ls
from . import ip_move   # Move/rename IP around project structure (if many dirs have IPs) or to another project altogether (also implements `cargo vendor`)
from . import ip_outdated
from . import ip_owner
from . import ip_pack
from . import ip_prune
from . import ip_publish
from . import ip_repo
from . import run_script
from . import ip_search
from . import set_script
from . import ip_shrinkwrap   # Creates/updates ip.lock.yml. Also implements cargo's 'verify-project'
from . import ip_star
from . import ip_stars
from . import ip_tag
from . import ip_test
from . import ip_uninstall
from . import ip_unpublish
from . import ip_update
from . import ip_version
from . import ip_view
########################################################################################################################


########################################################################################################################
# FUNCTIONS
########################################################################################################################
def main(up_args):
    args = docopt(__doc__, argv=up_args)
    argv = [args['<command>']] + args['<args>']

    if args['<command>'] == 'access':
        print(docopt(ip_access.__doc__, argv=argv))
    elif args['<command>'] == 'bugs':
        print(docopt(ip_bugs.__doc__, argv=argv))
    elif args['<command>'] == 'cache':
        print(docopt(ip_cache.__doc__, argv=argv))
    elif args['<command>'] == 'ci':
        print(docopt(ip_ci.__doc__, argv=argv))
    elif args['<command>'] == 'copy':
        print(docopt(ip_copy.__doc__, argv=argv))
    elif args['<command>'] == 'dedupe':
        print(docopt(ip_dedupe.__doc__, argv=argv))
    elif args['<command>'] == 'deprecate':
        print(docopt(ip_deprecate.__doc__, argv=argv))
    elif args['<command>'] == 'diff':
        print(docopt(ip_diff.__doc__, argv=argv))
    elif args['<command>'] == 'docs':
        print(docopt(ip_docs.__doc__, argv=argv))
    elif args['<command>'] == 'edit':
        print(docopt(ip_edit.__doc__, argv=argv))
    elif args['<command>'] == 'explain':
        print(docopt(ip_explain.__doc__, argv=argv))
    elif args['<command>'] == 'explore':
        print(docopt(ip_explore.__doc__, argv=argv))
    elif args['<command>'] == 'fund':
        print(docopt(ip_fund.__doc__, argv=argv))
    elif args['<command>'] == 'hook':
        print(docopt(ip_hook.__doc__, argv=argv))
    elif args['<command>'] == 'init':
        print(docopt(ip_init.__doc__, argv=argv))
    elif args['<command>'] == 'install':
        print(docopt(ip_install.__doc__, argv=argv))
    elif args['<command>'] == 'ls':
        print(docopt(ip_ls.__doc__, argv=argv))
    elif args['<command>'] == 'move':
        print(docopt(ip_move.__doc__, argv=argv))
    elif args['<command>'] == 'outdated':
        print(docopt(ip_outdated.__doc__, argv=argv))
    elif args['<command>'] == 'owner':
        print(docopt(ip_owner.__doc__, argv=argv))
    elif args['<command>'] == 'pack':
        print(docopt(ip_pack.__doc__, argv=argv))
    elif args['<command>'] == 'prune':
        print(docopt(ip_prune.__doc__, argv=argv))
    elif args['<command>'] == 'publish':
        print(docopt(ip_publish.__doc__, argv=argv))
    elif args['<command>'] == 'repo':
        print(docopt(ip_repo.__doc__, argv=argv))
    elif args['<command>'] == 'run-script':
        print(docopt(run_script.__doc__, argv=argv))
    elif args['<command>'] == 'search':
        print(docopt(ip_search.__doc__, argv=argv))
    elif args['<command>'] == 'set-script':
        print(docopt(set_script.__doc__, argv=argv))
    elif args['<command>'] == 'shrinkwrap':
        print(docopt(ip_shrinkwrap.__doc__, argv=argv))
    elif args['<command>'] == 'star':
        print(docopt(ip_star.__doc__, argv=argv))
    elif args['<command>'] == 'stars':
        print(docopt(ip_stars.__doc__, argv=argv))
    elif args['<command>'] == 'tag':
        print(docopt(ip_tag.__doc__, argv=argv))
    elif args['<command>'] == 'test':
        print(docopt(ip_test.__doc__, argv=argv))
    elif args['<command>'] == 'uninstall':
        print(docopt(ip_uninstall.__doc__, argv=argv))
    elif args['<command>'] == 'unpublish':
        print(docopt(ip_unpublish.__doc__, argv=argv))
    elif args['<command>'] == 'update':
        print(docopt(ip_update.__doc__, argv=argv))
    elif args['<command>'] == 'version':
        print(docopt(ip_version.__doc__, argv=argv))
    elif args['<command>'] == 'view':
        print(docopt(ip_view.__doc__, argv=argv))
    else:
        exit_error(args['<command>'])


def exit_error(command):
    sys.exit("'ip {}' is not an mio command. See 'mio help'.".format(command))
########################################################################################################################
