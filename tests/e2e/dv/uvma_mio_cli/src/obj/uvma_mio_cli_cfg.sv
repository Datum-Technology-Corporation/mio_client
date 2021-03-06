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


`ifndef __UVMA_MIO_CLI_CFG_SV__
`define __UVMA_MIO_CLI_CFG_SV__


/**
 * Object encapsulating all parameters for creating, connecting and running all Moore.io CLI Testing Grounds agent (uvma_mio_cli_agent_c) components.
 */
class uvma_mio_cli_cfg_c extends uvm_object;
   
   // Generic options
   rand bit                      enabled          ;
   rand uvm_active_passive_enum  is_active        ;
   rand uvml_reset_type_enum     reset_type       ;
   rand uvm_sequencer_arb_mode   sqr_arb_mode     ;
   rand bit                      cov_model_enabled;
   rand bit                      trn_log_enabled  ;
   
   
   `uvm_object_utils_begin(uvma_mio_cli_cfg_c)
      `uvm_field_int (                         enabled          , UVM_DEFAULT)
      `uvm_field_enum(uvm_active_passive_enum, is_active        , UVM_DEFAULT)
      `uvm_field_enum(uvml_reset_type_enum   , reset_type       , UVM_DEFAULT)
      `uvm_field_enum(uvm_sequencer_arb_mode , sqr_arb_mode     , UVM_DEFAULT)
      `uvm_field_int (                         cov_model_enabled, UVM_DEFAULT)
      `uvm_field_int (                         trn_log_enabled  , UVM_DEFAULT)
   `uvm_object_utils_end
   
   
   constraint defaults_cons {
      soft enabled           == 1;
      soft is_active         == UVM_PASSIVE;
      soft reset_type        == UVML_RESET_TYPE_SYNCHRONOUS;
      soft sqr_arb_mode      == UVM_SEQ_ARB_FIFO;
      soft cov_model_enabled == 0;
      soft trn_log_enabled   == 1;
   }
   
   
   /**
    * Default constructor.
    */
   extern function new(string name="uvma_mio_cli_cfg");
   
endclass : uvma_mio_cli_cfg_c


function uvma_mio_cli_cfg_c::new(string name="uvma_mio_cli_cfg");
   
   super.new(name);
   
endfunction : new


`endif // __UVMA_MIO_CLI_CFG_SV__
