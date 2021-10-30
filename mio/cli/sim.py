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


"""Moore.io Sim(ulation) Command
   Performs necessary steps to run simulation of an IP. Supports Digital and Mixed-Signal (AMS) Simulation.
   
   While the controls for individual steps (library creation, compilation, elaboration and simulation) are exposed, it
   is recommended to let `mio sim` manage this process as much as possible.  In the unlikely event of corrupt and/or
   locked simulator artifacts, see `mio clean`.  Combining any of the step-control arguments (-L, -C, -E, -S) with
   missing steps can result in unpredictable behavior and is not recommended (ex: `-LS`).
   
   Parameters (`<params>`) are parsed by mio which performs the conversions to specific vendor tool arguments, as
   specified by IP metadata (`ip.yml`) and the Configuration Database (`.mio.toml`).  Parameters that are not
   recognized are passed untouched to the end executable, along with all Tool Arguments (`<args>`).
   
   Unless configured otherwise, mio will attempt to parallelize every step of the process as much as the IP dependency
   graph and computing resources allow.  Job Scheduling setup is captured via `mio config`.
   
   For small runs of the same test, the combination of `--batch-mode` and `--repeat` (with the absence of `--seed`) is
   recommended over adding temporarily to an IP's test suite. Ex: `mio sim my_ip -t my_test --batch --repeat=10`
   
   Sim can accept multiple 'mlist' files. The following is a sample to be used with `--m-file`:
   ```
   % mio@0.2.1
      --config-env='simulators.questa.12.1.path'=QUESTA_12_1_DIR
      --config=abc=123
   $ sim
      @my_scope/my_ip@2.1.0-rc.2
      --test=my_test
      --seed=23948324
      --waves='/dp/egress/*'
      --app=questa@12.1
   --
      dp-width=32B
      phy-bypass=yes
      +define+TEMP_FIX=1  # Single line comments are allowed
      +NUM_PKTS=232
      +MIN_PKT_SIZE=32
      +MAX_PKT_SIZE=500
   ---
      --permissive
      --hotfix232
   ```

Usage:
   mio sim [[@<scope>/]<ip>[@<version>]] [options] [-- <params>] [--- <args>]  Runs specific simulation
   mio sim !                             [options] [-- <params>] [--- <args>]  Re-runs last simulation

Options:
   -t <name>      , --test=<name>         Specifies test name (for UVM/VMM/OVM based IPs).
   -s <integer>   , --seed=<integer>      Specifies simulation seed.  A random one will be chosen if not specified.
   -v <level>     , --verbosity=<level>   Specifies verbosity level (for UVM/VMM/OVM based IPs).
   -w [<selector>], --waves[=<selector>]  Captures simulation waveforms with optional selector. [default: '*']
   -c <flags>     , --cov=<flags>         Specifies coverage types to be collected: b,c,f,s,t,x or * (all) (ex: 'bct').
   -a <name>      , --app=<name>          Specifies simulator application name (must be in mio Configuration).
   -g             , --gui                 Invokes simulator in graphical or 'GUI' mode.
   
   -f <path>, --m-file=<path>      Specifies mlist from which to load mio arguments, IP parameters and Tool arguments.
   -x <path>, --tcl-script=<path>  Specifies TCL script to be executed by simulator.
   -z <path>, --snapshot=<path>    Specifies simulation snapshot to be loaded.
   -n <path>, --netlist=<path>     Specifies design netlist to use.
   -i <path>, --sdf=<path>         Specifies timing annotations file to use for netlist.
   
   -L, --library-creation-only  Only creates simulator libraries for each IP.
   -C, --compilation-only       Only performs compilation of each IP.
   -E, --elaboration-only       Only performs elaboration for target IP.
   -S, --simulation-only        Only launches simulation for target IP.
   -F, --force-steps            Forces mio to go through all the steps necessary.
   
   -l <string> , --label=<string>      Specifies results label.  Used as a prefix/suffix in file and/or directory names.
   -q          , --quiet               Mutes simulator output to stdout.
   -b          , --batch-mode          Runs simulations in parallel (usually combined with --repeat).
   -r <integer>, --repeat=<integer>    Specifies number of simulation repeats. [default: 1]
   -p <path>   , --results-dir=<path>  Specifies results directory path.  A symlink is created in the local results.
   -d          , --dry-run             Only prints the commands mio would normally execute to perform simulation.
   -m          , --m-run               Only prints the mlist file contents for the mio command.

Examples:
   mio sim !                                            # Re-run last simulation
   mio sim --test=my_test --seed=42 --verbosity=high    # Simulate Default IP with specific test, seed and verbosity
   mio sim -l bug_dbg -f ./bug35.mlist                  # Simulate using arguments file and a simulation label
   mio sim my_ip -CE -- dp-width=32B --- --permissive   # Compile and elaborate specific IP with IP parameter and tool
                                                          argument
   mio sim some_ip -t my_test -a vcs -x dbg_sigs.tcl    # Run a specific test with VCS and a specific TCL script
   mio sim -S -t my_test -s 1 --waves='/my_block/*'     # Only simulate a specific test, seed with custom wave capture
   mio sim -a nc -n ./bin/latest.sv --sdf=default.sdf   # Simulate specific design netlist with specific delays with NC
   mio sim my_ip -t my_test -b --repeat=10 --cov=*      # Simulate a specific IP and test 10 times in parallel with
                                                          random seeds and all coverage types being collected
   mio sim ! -m > ./bug35.mlist                         # Create mlist file to reproduce simulation elsewhere with mio
   mio sim @my_scope/my_ip -a vcs -Cd > ./ip.vcs.flist  # Create filelist to reproduce simulation outside mio"""


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
   logging.debug("sim - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("sim - args: " + str(args))
########################################################################################################################
