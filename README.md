# Moore.io Platform CLI MVP
Moore.io Platform Command Line Interface (CLI) Client Market Viable Prototype (MVP)

````
                              ███╗   ███╗ ██████╗  ██████╗ ██████╗ ███████╗   ██╗ ██████╗
                              ████╗ ████║██╔═══██╗██╔═══██╗██╔══██╗██╔════╝   ██║██╔═══██╗
                              ██╔████╔██║██║   ██║██║   ██║██████╔╝█████╗     ██║██║   ██║
                              ██║╚██╔╝██║██║   ██║██║   ██║██╔══██╗██╔══╝     ██║██║   ██║
                              ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██║  ██║███████╗██╗██║╚██████╔╝
                              ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚═╝ ╚═════╝ 
                                     Moore.io (`mio`) Command Line Interface (CLI)
                                           I N T E R A C T I V E   D E M O

Usage:
   mio [--version] [--help] [--list-commands]
   mio [--html-path] [--man-path] [--info-path]
   mio [--wd=<path>] [--config=<name>=<value>] [--config-env=<name>=<envvar>]
       [-p | --paginate | -P | --no-pager]
       [--dbg=<level>]
       <command> [<args> ...]

Options:
   -v, --version
      Prints the mio version and exits.
   
   -h, --help
      Prints the overall synopsis and a list of the most commonly used commands and exits.
   
   --list-commands
      Prints a list of all mio commands and exits.
      
   -C <path>, --wd=<path>
      Run as if mio was started in <path> instead of the current working directory.  When multiple -C options are
      given, each subsequent non-absolute -C <path> is interpreted relative to the preceding -C <path>.  If <path> is
      present but empty, e.g. -C "", then the current working directory is left unchanged.
   
   -c <name>=<value>, --config=<name>=<value>
      Pass a configuration parameter to the command.  The value given will override values from configuration files.
      The <name> is expected in the same format as listed by `mio config` (subkeys separated by dots).
      
      Note that omitting the `=` in `mio -c foo.bar ...` is allowed and sets `foo.bar` to the boolean true value (just
      like `[foo]bar` would in a config file).  Including the equals but with an empty value (like
      `mio -c foo.bar= ...`) sets foo.bar to the empty string which `mio config --type=bool` will convert to `false`.
      
   --config-env=<name>=<envvar>
      Like `-c <name>=<value>`, give configuration variable <name> a value, where <envvar> is the name of an
      environment variable from which to retrieve the value.  Unlike `-c` there is no shortcut for directly setting the
      value to an empty string, instead the environment variable itself must be set to the empty string.  It is an
      error if the `<envvar>` does not exist in the environment.  `<envvar>` may not contain an equals sign to avoid
      ambiguity with `<name>` containing one.
   
   --html-path
      Prints the path, without trailing slash, where mio's HTML documentation is installed and exits.
   
   --man-path
      Prints the manpath (see `man(1)`) for the man pages for this version of Moore.io and exits.
   
   --info-path
      Prints the path where the Info files documenting this version of mio are installed and exits.
   
   -p, --paginate
      Pipe all output into less (or if set, $PAGER) if standard output is a terminal.
   
   -P, --no-pager
      Do not pipe mio output into a pager.
    
   --dbg=<level>
      Enables debugging and tracing outputs from mio. [default: 0]

Full Command List:
   Help and Shell/Editor Integration
      help           Documentation for all mio commands
      help-search    Searches mio documentation for the terms provided and lists the results by relevance.
      doctor         Runs a set of checks to ensure mio installation has what it needs to operate properly
      completion     Produces outputs for shell/editor tab completion of mio commands and contents
   
   Project and Environment Management
      init           Starts project creation dialog
      config         Reads/writes to/from mio configuration space
      new            Creates new source code via the mio template engine
      vcs            Automates version control system tasks
   
   IP and Credentials Management
      ip             Creates, modify and manage IPs
      org            Manages organizations
      team           Manages teams
      user           Manages users
   
   Automate Moore.io, F&OS and Vendor EDA Tools
      sim            Performs necessary steps to simulate IP
      regr           Runs regression(s) against IP(s)
      lint           Executes hdl linting tool(s) against IP(s)
      synth          Executes logic synthesis tool(s) against IP(s)
      timing         Executes timing analysis tool(s) against IP(s)
      formal         Executes formal logic verification tool(s) against IP(s)
      emul           Launches emulation engine(s) against IP(s)
      hdl-connect    HDL source code port connection/disconnection
      hdl-doc        HDL source code documentation generator
      hdl-refactor   HDL re-factorization engine
      hdl-style      HDL source code style policy enforcer
      
   Manage Results and other EDA Tool Outputs
      results        Manages results from EDA tools
      clean          Manages outputs from tools (other than job results)
````