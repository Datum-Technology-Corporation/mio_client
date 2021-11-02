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


`ifndef __UVMA_MIO_CLI_SEQ_ITEM_SV__
`define __UVMA_MIO_CLI_SEQ_ITEM_SV__


/**
 * Object created by Moore.io CLI Testing Grounds agent sequences extending uvma_mio_cli_seq_base_c.
 */
class uvma_mio_cli_seq_item_c extends uvml_seq_item_c;
   
   // TODO Add uvma_mio_cli_seq_item_c fields
   //      Ex: rand bit [7:0]  abc;
   
   // Metadata
   uvma_mio_cli_cfg_c  cfg;
   
   
   `uvm_object_utils_begin(uvma_mio_cli_seq_item_c)
      // TODO Add uvma_mio_cli_seq_item_c UVM field utils
      //      Ex: `uvm_field_int(abc, UVM_DEFAULT)
   `uvm_object_utils_end
   
   
   // TODO Add uvma_mio_cli_seq_item_c constraints
   //      Ex: constraint default_cons {
   //             abc inside {0,2,4,8,16,32};
   //          }
   
   
   /**
    * Default constructor.
    */
   extern function new(string name="uvma_mio_cli_seq_item");
   
endclass : uvma_mio_cli_seq_item_c


function uvma_mio_cli_seq_item_c::new(string name="uvma_mio_cli_seq_item");
   
   super.new(name);
   
endfunction : new


`endif // __UVMA_MIO_CLI_SEQ_ITEM_SV__
