// Copyright 2021 Datum Technology Corporation
// SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


`ifndef __UVME_MIO_CLI_ST_PKG_SV__
`define __UVME_MIO_CLI_ST_PKG_SV__


// Pre-processor macros
`include "uvm_macros.svh"
`include "uvml_macros.svh"
`include "uvml_logs_macros.svh"
`include "uvml_sb_macros.svh"
`include "uvma_mio_cli_macros.svh"
`include "uvme_mio_cli_st_macros.svh"

// Interface(s)


 /**
 * Encapsulates all the types needed for an UVM environment capable of self-testing the Moore.io CLI Testing Grounds.
 */
package uvme_mio_cli_st_pkg;

   import uvm_pkg         ::*;
   import uvml_pkg        ::*;
   import uvml_logs_pkg   ::*;
   import uvml_sb_pkg     ::*;
   import uvma_mio_cli_pkg::*;

   // Constants / Structs / Enums
   `include "uvme_mio_cli_st_tdefs.sv"
   `include "uvme_mio_cli_st_constants.sv"

   // Objects
   `include "uvme_mio_cli_st_cfg.sv"
   `include "uvme_mio_cli_st_cntxt.sv"

   // Environment components
   `include "uvme_mio_cli_st_cov_model.sv"
   `include "uvme_mio_cli_st_prd.sv"
   `include "uvme_mio_cli_st_vsqr.sv"
   `include "uvme_mio_cli_st_env.sv"

   // Sequences
   `include "uvme_mio_cli_st_vseq_lib.sv"

endpackage : uvme_mio_cli_st_pkg


// Module(s) / Checker(s)
`ifdef UVME_MIO_CLI_ST_INC_CHKR
`include "uvme_mio_cli_st_chkr.sv"
`endif


`endif // __UVME_MIO_CLI_ST_PKG_SV__
