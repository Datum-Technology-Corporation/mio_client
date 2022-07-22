# Moore.io CLI Client
## About
The Moore.io Command Line Interface (CLI) Client is a toolchain for front-end engineering of FPGA/ASIC projects.

## Building documentation
````
cd docs
make html
firefox ./_build/html/index.html
````

## Usage
````
  mio install  <ip> [-g | --global]  [-u <username>]  [-p <password>]
  mio sim      <ip> [-C] [-E] [-S] [-t <test_name>]  [-s <seed>]  [-v <level>]  [-g | --gui]  [-w | --waves]  [-c | --cov] [-- <args>]
  mio clean
  mio results  <ip> <filename>
  mio cov      <ip>
  mio dox      <ip>
  mio (-h | --help)
  mio --version

Options:
  -h --help     Show this screen.
  --version     Show version.
   
Examples:
  mio install   uvmt_my_ip   # Installs IP dependencies from Moore.io IP Marketplace.
  
  mio sim -C  uvmt_my_ip                 # Only compile test bench for uvmt_my_ip
  mio sim -E  uvmt_my_ip                 # Only elaborate test bench for uvmt_my_ip
  mio sim -CE uvmt_my_ip                 # Compile and elaborate test bench for uvmt_my_ip
  mio sim -S  uvmt_my_ip -t smoke -s 1   # Only simulates test 'uvmt_my_ip_smoke_test_c' for top-level module 'uvmt_my_ip_tb'
  mio sim     uvmt_my_ip -t smoke -s 1   # Compiles, elaborates and simulates test 'uvmt_my_ip_smoke_test_c' for bench 'uvmt_my_ip'
  
  mio clean                  # Deletes all simulation artifacts
  mio results   uvmt_my_ip   # Parses simulation results and generates report from an IP's simulations
  mio cov       uvmt_my_ip   # Merges coverage data and generates reports from an IP's simulations
  mio dox       uvmt_my_ip   # Invokes Doxygen to generates reference documentation for an IP
````
