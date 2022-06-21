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
 * This file contains sample code that demonstrates how to add a new sequence to the Moore.io CLI Testing Grounds UVM Agent.
 */


`ifndef __UVMA_MIO_CLI_MY_SEQ_SV__
`define __UVMA_MIO_CLI_MY_SEQ_SV__


/**
 * Sample sequence that runs 5 fully random items by default.
 */
class uvma_mio_cli_my_seq_c extends uvma_mio_cli_base_seq_c;
   
   // Fields
   rand int unsigned  num_items;
   
   
   `uvm_object_utils_begin(uvma_mio_cli_my_seq_c)
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
   extern function new(string name="uvma_mio_cli_my_seq");
   
   /**
    * Generates num_items of fully random reqs.
    */
   extern virtual task body();
   
endclass : uvma_mio_cli_my_seq_c


function uvma_mio_cli_my_seq_c::new(string name="uvma_mio_cli_my_seq");
   
   super.new(name);
   
endfunction : new


task uvma_mio_cli_my_seq_c::body();
   
   repeat (num_items) begin
      `uvm_do(req)
   end
   
endtask : body


`endif __UVMA_MIO_CLI_MY_SEQ_SV__
