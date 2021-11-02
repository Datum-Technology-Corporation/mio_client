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


`ifndef __UVME_MIO_CLI_ST_CNTXT_SV__
`define __UVME_MIO_CLI_ST_CNTXT_SV__


/**
 * Object encapsulating all state variables for Moore.io CLI Testing Grounds  Self-Testing environment (uvme_mio_cli_st_env_c) components.
 */
class uvme_mio_cli_st_cntxt_c extends uvm_object;
   
   // Agent context handles
   uvma_mio_cli_cntxt_c  bob_cntxt;
   uvma_mio_cli_cntxt_c  alice_cntxt;
   
   // Scoreboard context handle
   uvml_sb_simplex_cntxt_c  sb_cntxt;
   
   // Events
   uvm_event  sample_cfg_e  ;
   uvm_event  sample_cntxt_e;
   
   
   `uvm_object_utils_begin(uvme_mio_cli_st_cntxt_c)
      `uvm_field_object(bob_cntxt, UVM_DEFAULT)
      `uvm_field_object(alice_cntxt, UVM_DEFAULT)
      
      `uvm_field_object(sb_cntxt, UVM_DEFAULT)
      
      `uvm_field_event(sample_cfg_e  , UVM_DEFAULT)
      `uvm_field_event(sample_cntxt_e, UVM_DEFAULT)
   `uvm_object_utils_end
   
   
   /**
    * Builds events and sub-context objects.
    */
   extern function new(string name="uvme_mio_cli_st_cntxt");
   
   /**
    * TODO Describe uvme_mio_cli_st_cntxt_c::reset()
    */
   extern function void reset();
   
endclass : uvme_mio_cli_st_cntxt_c


function uvme_mio_cli_st_cntxt_c::new(string name="uvme_mio_cli_st_cntxt");
   
   super.new(name);
   
   bob_cntxt = uvma_mio_cli_cntxt_c::type_id::create("bob_cntxt");
   alice_cntxt = uvma_mio_cli_cntxt_c::type_id::create("alice_cntxt");
   sb_cntxt = uvml_sb_simplex_cntxt_c::type_id::create("sb_cntxt");
   
   sample_cfg_e   = new("sample_cfg_e"  );
   sample_cntxt_e = new("sample_cntxt_e");
   
endfunction : new


function void uvme_mio_cli_st_cntxt_c::reset();
   
   bob_cntxt.reset();
   alice_cntxt.reset();
   
endfunction : reset


`endif // __UVME_MIO_CLI_ST_CNTXT_SV__
