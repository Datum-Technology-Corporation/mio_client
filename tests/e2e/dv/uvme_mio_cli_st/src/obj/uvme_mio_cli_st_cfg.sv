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


`ifndef __UVME_MIO_CLI_ST_CFG_SV__
`define __UVME_MIO_CLI_ST_CFG_SV__


/**
 * Object encapsulating all parameters for creating, connecting and running Moore.io CLI Testing Grounds Self-Testing Environment (uvme_mio_cli_st_env_c) components.
 */
class uvme_mio_cli_st_cfg_c extends uvm_object;
   
   // Integrals
   rand bit                      enabled              ;
   rand uvm_active_passive_enum  is_active            ;
   rand bit                      scoreboarding_enabled;
   rand bit                      cov_model_enabled    ;
   rand bit                      trn_log_enabled      ;
   
   // Objects
   rand uvma_mio_cli_cfg_c     alice_cfg;
   rand uvma_mio_cli_cfg_c     bob_cfg  ;
   rand uvml_sb_simplex_cfg_c  sb_cfg   ;
   
   
   `uvm_object_utils_begin(uvme_mio_cli_st_cfg_c)
      `uvm_field_int (                         enabled              , UVM_DEFAULT)
      `uvm_field_enum(uvm_active_passive_enum, is_active            , UVM_DEFAULT)
      `uvm_field_int (                         scoreboarding_enabled, UVM_DEFAULT)
      `uvm_field_int (                         cov_model_enabled    , UVM_DEFAULT)
      `uvm_field_int (                         trn_log_enabled      , UVM_DEFAULT)
      
      `uvm_field_object(alice_cfg, UVM_DEFAULT)
      `uvm_field_object(bob_cfg  , UVM_DEFAULT)
      `uvm_field_object(sb_cfg   , UVM_DEFAULT)
   `uvm_object_utils_end
   
   
   constraint defaults_cons {
      soft enabled                == 0;
      soft is_active              == UVM_PASSIVE;
      soft scoreboarding_enabled  == 1;
      soft cov_model_enabled      == 0;
      soft trn_log_enabled        == 1;
   }
   
   constraint agent_cfg_cons {
      if (enabled) {
         bob_cfg.enabled == 1;
         alice_cfg.enabled == 1;
      }
      else {
         bob_cfg.enabled == 0;
         alice_cfg.enabled == 0;
      }
      
      if (is_active == UVM_ACTIVE) {
         bob_cfg.is_active == UVM_ACTIVE;
         alice_cfg.is_active == UVM_ACTIVE;
      }
      else {
         bob_cfg.is_active == UVM_PASSIVE;
         alice_cfg.is_active == UVM_PASSIVE;
      }
      
      if (trn_log_enabled) {
         bob_cfg.trn_log_enabled == 1;
         alice_cfg.trn_log_enabled == 1;
      }
      else {
         bob_cfg.trn_log_enabled == 0;
         alice_cfg.trn_log_enabled == 0;
      }
      
      if (cov_model_enabled) {
         bob_cfg.cov_model_enabled == 1;
         alice_cfg.cov_model_enabled == 1;
      }
      else {
         bob_cfg.cov_model_enabled == 0;
         alice_cfg.cov_model_enabled == 0;
      }
   }
   
   constraint sb_cfg_cons {
      sb_cfg.mode == UVML_SB_MODE_IN_ORDER;
      if (scoreboarding_enabled) {
         sb_cfg.enabled == 1;
      }
      else {
         sb_cfg.enabled == 0;
      }
   }
   
   
   /**
    * Creates sub-configuration objects.
    */
   extern function new(string name="uvme_mio_cli_st_cfg");
   
endclass : uvme_mio_cli_st_cfg_c


function uvme_mio_cli_st_cfg_c::new(string name="uvme_mio_cli_st_cfg");
   
   super.new(name);
   
   bob_cfg  = uvma_mio_cli_cfg_c::type_id::create("bob_cfg");
   alice_cfg  = uvma_mio_cli_cfg_c::type_id::create("alice_cfg");
   sb_cfg = uvml_sb_simplex_cfg_c::type_id::create("sb_cfg");
   
endfunction : new


`endif // __UVME_MIO_CLI_ST_CFG_SV__
