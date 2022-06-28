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
Usage:
  mio all  <target>  [-t <test_name>]  [-s <seed>]  [-v <level>]  [-g | --gui]  [-w | --waves]  [-q | --noclean]  [-c | --cov] [-- <args>]
  mio cmp  <target>
  mio elab <target>  [-d | --debug]
  mio cpel <target>
  mio sim  <target>  [-t <test_name>]  [-s <seed>]  [-v <level>]  [-g | --gui]  [-w | --waves]  [-c | --cov] [-- <args>]
  mio clean
  mio results    <target> <filename>
  mio cov        <target>
  mio dox <name> <target>
  mio (-h | --help)
  mio --version

Options:
  -h --help     Show this screen.
  --version     Show version.
   
Examples:
  mio clean                          # Deletes all simulation artifacts and results
  
  mio cmp  uvmt_my_ip                # Only compile test bench for uvmt_my_ip
  mio elab uvmt_my_ip                # Only elaborate test bench for uvmt_my_ip
  mio cpel uvmt_my_ip                # Compile and elaborate test bench for uvmt_my_ip
  mio sim  uvmt_my_ip -t smoke -s 1  # Only simulates test 'uvmt_my_ip_smoke_test_c' for top-level module 'uvmt_my_ip_tb'
  
  mio all uvmt_my_ip -t smoke -s 1   # Compiles, elaborates and simulates test 'uvmt_my_ip_smoke_test_c' for bench 'uvmt_my_ip'
````
