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


`ifndef __UVMA_MIO_CLI_DRV_SV__
`define __UVMA_MIO_CLI_DRV_SV__


/**
 * Component driving a Moore.io CLI Testing Grounds virtual interface (uvma_mio_cli_if).
 */
class uvma_mio_cli_drv_c extends uvm_driver #(
   .REQ(uvma_mio_cli_seq_item_c),
   .RSP(uvma_mio_cli_seq_item_c)
);
   
   // Objects
   uvma_mio_cli_cfg_c    cfg;
   uvma_mio_cli_cntxt_c  cntxt;
   
   // TLM
   uvm_analysis_port#(uvma_mio_cli_seq_item_c)  ap;
   
   // Handle(s) to virtual interface modport(s)
   virtual uvma_mio_cli_if.drv_mp  mp;
   
   
   `uvm_component_utils_begin(uvma_mio_cli_drv_c)
      `uvm_field_object(cfg  , UVM_DEFAULT)
      `uvm_field_object(cntxt, UVM_DEFAULT)
   `uvm_component_utils_end
   
   
   /**
    * Default constructor.
    */
   extern function new(string name="uvma_mio_cli_drv", uvm_component parent=null);
   
   /**
    * 1. Ensures cfg & cntxt handles are not null.
    * 2. Builds ap.
    */
   extern virtual function void build_phase(uvm_phase phase);
   
   /**
    * Oversees driving, depending on the reset state, by calling drv_<pre|in|post>_reset() tasks.
    */
   extern virtual task run_phase(uvm_phase phase);
   
   /**
    * Called by run_phase() while agent is in pre-reset state.
    */
   extern virtual task drv_pre_reset();
   
   /**
    * Called by run_phase() while agent is in reset state.
    */
   extern virtual task drv_in_reset();
   
   /**
    * Called by run_phase() while agent is in post-reset state.
    */
   extern virtual task drv_post_reset();
   
   /**
    * Appends cfg, prints out trn and issues heartbeat.
    */
   extern virtual function void process_req(ref uvma_mio_cli_seq_item_c req);
   
   /**
    * Drives the virtual interface's (cntxt.vif) signals using req's contents.
    */
   extern virtual task drv_req(ref uvma_mio_cli_seq_item_c req);
   
endclass : uvma_mio_cli_drv_c


function uvma_mio_cli_drv_c::new(string name="uvma_mio_cli_drv", uvm_component parent=null);
   
   super.new(name, parent);
   
endfunction : new


function void uvma_mio_cli_drv_c::build_phase(uvm_phase phase);
   
   super.build_phase(phase);
   
   void'(uvm_config_db#(uvma_mio_cli_cfg_c)::get(this, "", "cfg", cfg));
   if (!cfg) begin
      `uvm_fatal("CFG", "Configuration handle is null")
   end
   uvm_config_db#(uvma_mio_cli_cfg_c)::set(this, "*", "cfg", cfg);
   
   void'(uvm_config_db#(uvma_mio_cli_cntxt_c)::get(this, "", "cntxt", cntxt));
   if (!cntxt) begin
      `uvm_fatal("CNTXT", "Context handle is null")
   end
   uvm_config_db#(uvma_mio_cli_cntxt_c)::set(this, "*", "cntxt", cntxt);
   
   ap = new("ap", this);
   mp = cntxt.vif.drv_mp;
   
endfunction : build_phase


task uvma_mio_cli_drv_c::run_phase(uvm_phase phase);
   
   super.run_phase(phase);
   
   if (cfg.enabled && cfg.is_active) begin
      forever begin
         case (cntxt.reset_state)
            UVML_RESET_STATE_PRE_RESET : drv_pre_reset ();
            UVML_RESET_STATE_IN_RESET  : drv_in_reset  ();
            UVML_RESET_STATE_POST_RESET: drv_post_reset();
         endcase
      end
   end
   
endtask : run_phase


task uvma_mio_cli_drv_c::drv_pre_reset();
   
   @(mp.drv_cb);
   
endtask : drv_pre_reset


task uvma_mio_cli_drv_c::drv_in_reset();
   
   @(mp.drv_cb);
   
endtask : drv_in_reset


task uvma_mio_cli_drv_c::drv_post_reset();
   
   seq_item_port.get_next_item(req);
   process_req                (req);
   drv_req                    (req);
   ap.write                   (req);
   
   seq_item_port.item_done();
   
endtask : drv_post_reset


function void uvma_mio_cli_drv_c::process_req(ref uvma_mio_cli_seq_item_c req);
   
   req.cfg = cfg;
   `uvm_info("${name_uppecase}_DRV", $sformatf("Got new req from the sequencer:\n%s", req.sprint()), UVM_HIGH)
   `uvml_hrtbt()
   
endfunction : process_req


task uvma_mio_cli_drv_c::drv_req(ref uvma_mio_cli_seq_item_c req);
   
   // TODO Implement uvma_mio_cli_drv_c::drv_req()
   //      Ex: @(mp.drv_cb);
   //          mp.drv_cb.enable <= 1'b1;
   //          mp.drv_cb.abc   <= req.abc;
   //          mp.drv_cb.xyz   <= req.xyz;
   
   // WARNING If no time is consumed by this task, a zero-delay oscillation loop will occur and stall simulation
   
endtask : drv_req


`endif // __UVMA_MIO_CLI_DRV_SV__
