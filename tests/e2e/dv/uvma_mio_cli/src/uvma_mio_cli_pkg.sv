// Copyright 2021 Datum Technology Corporation
// SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


`ifndef __UVMA_MIO_CLI_PKG_SV__
`define __UVMA_MIO_CLI_PKG_SV__


// Pre-processor macros
`include "uvm_macros.svh"
`include "uvml_macros.svh"
`include "uvml_logs_macros.svh"
`include "uvma_mio_cli_macros.svh"

// Interface(s)
`include "uvma_mio_cli_if.sv"


/**
 * Encapsulates all the types needed for an UVM agent capable of driving and/or monitoring Moore.io CLI Testing Grounds.
 */
package uvma_mio_cli_pkg;

   import uvm_pkg      ::*;
   import uvml_pkg     ::*;
   import uvml_logs_pkg::*;

   // Constants / Structs / Enums
   `include "uvma_mio_cli_tdefs.sv"
   `include "uvma_mio_cli_constants.sv"

   // Objects
   `include "uvma_mio_cli_cfg.sv"
   `include "uvma_mio_cli_cntxt.sv"

   // High-level transactions
   `include "uvma_mio_cli_mon_trn.sv"
   `include "uvma_mio_cli_mon_trn_logger.sv"
   `include "uvma_mio_cli_seq_item.sv"
   `include "uvma_mio_cli_seq_item_logger.sv"

   // Agent components
   `include "uvma_mio_cli_cov_model.sv"
   `include "uvma_mio_cli_drv.sv"
   `include "uvma_mio_cli_mon.sv"
   `include "uvma_mio_cli_sqr.sv"
   `include "uvma_mio_cli_agent.sv"

   // Sequences
   `include "uvma_mio_cli_base_seq.sv"
   // TODO Add sequences to uvma_mio_cli_pkg

endpackage : uvma_mio_cli_pkg


// Module(s) / Checker(s)
`ifdef UVMA_MIO_CLI_INC_IF_CHKR
`include "uvma_mio_cli_if_chkr.sv"
`endif


`endif // __UVMA_MIO_CLI_PKG_SV__
