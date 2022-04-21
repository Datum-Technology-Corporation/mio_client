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


/**
 * This file contains sample code that demonstrates how to add a new virtual sequence to the Moore.io CLI Testing Grounds UVM Environment.
 */


`ifndef __UVME_MIO_CLI_MY_VSEQ_SV__
`define __UVME_MIO_CLI_MY_VSEQ_SV__


/**
 * Sample sequence that runs 5 fully random items by default.
 */
class uvme_mio_cli_my_vseq_c extends uvme_mio_cli_base_vseq_c;
   
   // Fields
   rand int unsigned  num_items;
   
   
   `uvm_object_utils_begin(uvme_mio_cli_my_vseq_c)
      `uvm_field_int(num_items, UVM_DEFAULT)
   `uvm_object_utils_end
   
   
   /**
    * Default values for random fields.
    */
   constraint defaults_cons {
      soft num_items == 5;
   }
   
   
   /**
    * Default constructor.
    */
   extern function new(string name="uvme_mio_cli_my_seq");
   
   /**
    * Generates num_items of fully random reqs.
    */
   extern virtual task body();
   
endclass : uvme_mio_cli_my_vseq_c


function uvme_mio_cli_my_vseq_c::new(string name="uvme_mio_cli_my_seq");
   
   super.new(name);
   
endfunction : new


task uvme_mio_cli_my_vseq_c::body();
   
   repeat (num_items) begin
      `uvm_do_on(req, p_sequencer.sub_sequencer)
   end
   
endtask : body


`endif __UVME_MIO_CLI_MY_VSEQ_SV__
