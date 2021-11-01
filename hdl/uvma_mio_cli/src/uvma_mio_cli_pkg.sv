// Copyright 2021 Datum Technology Corporation
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
// Licensed under the Solderpad Hardware License v 2.1 (the "License"); you may not use this file except in compliance
// with the License, or, at your option, the Apache License version 2.0.  You may obtain a copy of the License at
//                                        https://solderpad.org/licenses/SHL-2.1/
// Unless required by applicable law or agreed to in writing, any work distributed under the License is distributed on
// an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the License for the
// specific language governing permissions and limitations under the License.
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


`ifndef __UVMA_MIO_CLI_PKG_SV__
`define __UVMA_MIO_CLI_PKG_SV__


// Pre-processor macros
`include "uvm_macros.svh"
`include "uvml_macros.sv"
`include "uvml_logs_macros.sv"
`include "uvma_mio_cli_macros.sv"

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
