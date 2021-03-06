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


`ifndef __UVME_MIO_CLI_ST_PRD_SV__
`define __UVME_MIO_CLI_ST_PRD_SV__


/**
 * Component implementing transaction-based software model of Moore.io CLI Testing Grounds Self-Testing DUT.
 */
class uvme_mio_cli_st_prd_c extends uvm_component;
   
   // Objects
   uvme_mio_cli_st_cfg_c    cfg  ;
   uvme_mio_cli_st_cntxt_c  cntxt;
   
   // TLM
   uvm_analysis_export  #(uvma_mio_cli_mon_trn_c)  in_export;
   uvm_tlm_analysis_fifo#(uvma_mio_cli_mon_trn_c)  in_fifo  ;
   uvm_analysis_port    #(uvma_mio_cli_mon_trn_c)  out_ap   ;
   
   
   `uvm_component_utils_begin(uvme_mio_cli_st_prd_c)
      `uvm_field_object(cfg  , UVM_DEFAULT)
      `uvm_field_object(cntxt, UVM_DEFAULT)
   `uvm_component_utils_end
   
   
   /**
    * Default constructor.
    */
   extern function new(string name="uvme_mio_cli_st_prd", uvm_component parent=null);
   
   /**
    * TODO Describe uvme_mio_cli_st_prd_c::build_phase()
    */
   extern virtual function void build_phase(uvm_phase phase);
   
   /**
    * TODO Describe uvme_mio_cli_st_prd_c::connect_phase()
    */
   extern virtual function void connect_phase(uvm_phase phase);
   
   /**
    * TODO Describe uvme_mio_cli_st_prd_c::run_phase()
    */
   extern virtual task run_phase(uvm_phase phase);
   
endclass : uvme_mio_cli_st_prd_c


function uvme_mio_cli_st_prd_c::new(string name="uvme_mio_cli_st_prd", uvm_component parent=null);
   
   super.new(name, parent);
   
endfunction : new


function void uvme_mio_cli_st_prd_c::build_phase(uvm_phase phase);
   
   super.build_phase(phase);
   
   void'(uvm_config_db#(uvme_mio_cli_st_cfg_c)::get(this, "", "cfg", cfg));
   if (!cfg) begin
      `uvm_fatal("CFG", "Configuration handle is null")
   end
   
   void'(uvm_config_db#(uvme_mio_cli_st_cntxt_c)::get(this, "", "cntxt", cntxt));
   if (!cntxt) begin
      `uvm_fatal("CNTXT", "Context handle is null")
   end
   
   // Build TLM objects
   in_export  = new("in_export", this);
   in_fifo    = new("in_fifo"  , this);
   out_ap     = new("out_ap"   , this);
   
endfunction : build_phase


function void uvme_mio_cli_st_prd_c::connect_phase(uvm_phase phase);
   
   super.connect_phase(phase);
   
   // Connect TLM objects
   in_export.connect(in_fifo.analysis_export);
   
endfunction: connect_phase


task uvme_mio_cli_st_prd_c::run_phase(uvm_phase phase);
   
   uvma_mio_cli_mon_trn_c  in_trn, out_trn;
   
   super.run_phase(phase);
   
   forever begin
      // Get next transaction and copy it
      in_fifo.get(in_trn);
      out_trn = uvma_mio_cli_mon_trn_c::type_id::create("out_trn");
      out_trn.copy(in_trn);
      
      // TODO Implement uvme_mio_cli_st_prd_c::run_phase()
      
      // Send transaction to analysis port
      out_ap.write(out_trn);
   end
   
endtask: run_phase


`endif // __UVME_MIO_CLI_ST_PRD_SV__
