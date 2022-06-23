# Copyright Datum Technology Corporation
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
########################################################################################################################


import cfg
import clean
import cov
import dox
import elab
import history
import results
import sim
import vivado
import utilities
import discovery

import sys
import os
import yaml
import subprocess
import fusesoc
import argparse
import re
from yaml.loader import SafeLoader
from datetime import datetime
from fusesoc import main as fsoc
from jinja2 import Template


def add_cmp_to_history_log(snapshot, compilation_log_path):
    now = datetime.now()
    timestamp = now.strftime("%Y/%m/%d-%H:%M:%S")
    utilities.create_history_log()
    if (cfg.dbg):
        print("Updating history file at " + cfg.history_file_path)
    with open(cfg.history_file_path, 'r') as yamlfile:
        cur_yaml = yaml.load(yamlfile, Loader=SafeLoader) # Note the safe_load
        if not snapshot in cur_yaml:
            cur_yaml[snapshot] = {}
        cur_yaml[snapshot]['compilation_timestamp'] = timestamp
        cur_yaml[snapshot]['compilation_log_path'] = compilation_log_path
        if cur_yaml:
            with open(cfg.history_file_path, 'w') as yamlfile:
                yaml.dump(cur_yaml, yamlfile) # Also note the safe_dump




def do_cmp_rtl(target_design):
    if (dbg):
        print("Call to do_cmp_rtl(target_design='" + target_design + "'")
    




def cmp_rtl(ip_name, args):
    ip_path         = ""
    ip_type         = ""
    ip_file_path    = ""
    ip_metadata     = {}
    rtl_ip_metadata = {}
    rtl_ip_path     = ""
    
    if not os.path.exists(cfg.sim_results_dir):
        os.mkdir(cfg.sim_results_dir)
    
    if ip_name not in discovery.ip_paths:
        sys.exit("Failed to find IP '" + ip_name + "'.  Exiting.")
    else:
        ip_path     = discovery.ip_paths   [ip_name]
        ip_metadata = discovery.ip_metadata[ip_name]
        
    if 'dut' in ip_metadata:
        rtl_ip_name = ip_metadata['dut']['name']
        ip_type     = ip_metadata['dut']['ip-type']
        
        if rtl_ip_name not in ip_catalog:
            sys.exit("Failed to find RTL IP '" + rtl_ip_name + "'.  Exiting.")
        else:
            rtl_ip_path     = discovery.ip_paths[rtl_ip_name]
            rtl_src_path    = os.path.join(rtl_ip_path, rtl_ip_metadata["structure"]["src-path"])
        
        if ip_type == "mio":
            if 'sub-type' in ip_metadata['ip']:
                rtl_sub_type = ip_metadata['ip']['sub-type'].lower().strip()
            else:
                rtl_sub_type = "none"
            if (rtl_sub_type == "vivado"):
                rtl_lib_name = rtl_ip_metadata['hdl-src']['lib-name']
                xilinx_libs  = rtl_ip_metadata['hdl-src']['xilinx-libs']
                vlog_prj_file_path = rtl_ip_metadata['hdl-src']['vlog']
                vhdl_prj_file_path = rtl_ip_metadata['hdl-src']['vhdl']
                vlog_compilation_log_path = cfg.sim_results_dir + "/" + rtl_ip_name + ".xvlog.cmp.log"
                vhdl_compilation_log_path = cfg.sim_results_dir + "/" + rtl_ip_name + ".xvhdl.cmp.log"
                print("\033[1;35m*************")
                print("Compiling RTL")
                print("*************\033[0m")
                # TODO Add Support for simulators other than Vivado
                vivado.run_bin("xvlog", " --relax -prj " + rtl_ip_path + "/" + vlog_prj_file_path + " " + args + " --log " + vlog_compilation_log_path)
                vivado.run_bin("xvhdl", " --relax -prj " + rtl_ip_path + "/" + vhdl_prj_file_path + " --log " + vhdl_compilation_log_path)
                add_cmp_to_history_log(rtl_lib_name + ".xvlog", vlog_compilation_log_path)
                add_cmp_to_history_log(rtl_lib_name + ".xvhdl", vhdl_compilation_log_path)
            else:
                print("\033[1;35m*************")
                print("Compiling RTL")
                print("*************\033[0m")
                # TODO Add Support for simulators other than Vivado
                vlog_flist_file_path = os.path.join(rtl_src_path, rtl_ip_metadata["hdl-src"]["flist"]["vivado"])
                vlog_compilation_log_path = cfg.sim_results_dir + "/" + rtl_ip_name + ".xvlog.cmp.log"
                vivado.run_bin("xvlog", " --relax -sv -f " + vlog_flist_file_path + " " + args + " --log " + vlog_compilation_log_path)
                add_cmp_to_history_log(rtl_lib_name + ".xvlog", vlog_compilation_log_path)
        
        elif ip_type == "fsoc":
            if os.path.exists(ip_dir + "/" + rtl_ip_name + ".core"):
                ip_file_path = ip_dir + "/" + rtl_ip_name + ".core"
                fsoc_target = ip_metadata['dut']['target']
                fsoc_fname  = ip_metadata['dut']['full-name']
                print("Invoking FuseSoC: ip='" + rtl_ip_name + "' target='" + fsoc_target + "' + full-name='" + fsoc_fname + "'")
                #subprocess.call("fusesoc --cores-root " + ip_dir + "/.. run --target=" + fsoc_target + " --tool=xsim --setup --build " + fsoc_fname, shell=True)
                cores_root = cfg.rtl_path
                fsc_args = argparse.Namespace()
                fsc_args.setup  = True
                fsc_args.build  = False
                fsc_args.run    = False
                fsc_args.no_export  = True
                fsc_args.tool   = "xsim"
                fsc_args.target = fsoc_target
                fsc_args.system = fsoc_fname
                fsc_args.backendargs = ""
                fsc_args.system_name = ""
                fsc_args.build_root  = cfg.sim_output_dir + "/fsoc/" + rtl_ip_name
                fsc_args.flag = []
                fsc_cores_root = [cores_root]
                fusesoc.main.init_logging(False, False)
                fsc_cfg = fusesoc.main.Config()
                fsc_cm  = fusesoc.main.init_coremanager(fsc_cfg, fsc_cores_root)
                fusesoc.main.run(fsc_cm, fsc_args)
                vlog_compilation_log_path = cfg.sim_results_dir + "/" + rtl_ip_name + ".xvlog.cmp.log"
                
                file_path_partial_name = re.sub(r':', '_', fsoc_fname)
                eda_file_dir = cfg.sim_output_dir + "/fsoc/" + rtl_ip_name + "/sim-xsim"
                eda_file_path = eda_file_dir + "/" + file_path_partial_name + "_0.eda.yml"
                
                if os.path.exists(eda_file_path):
                    with open(eda_file_path, 'r') as edafile:
                        eda_yaml = yaml.load(edafile, Loader=SafeLoader)
                        if eda_yaml:
                            dirs    = []
                            files   = []
                            defines = []
                            for file in eda_yaml['files']:
                                if file['file_type'] == "systemVerilogSource":
                                    if 'is_include_file' in file:
                                        if 'include_path' in file:
                                            dirs.append(re.sub("../../../../rtl/.imports", cfg.rtl_libs_path, file['include_path']))
                                    else:
                                        files.append(re.sub("../../../../rtl/.imports", cfg.rtl_libs_path, file['name']))
                            
                            for param in eda_yaml['parameters']:
                                if eda_yaml['parameters'][param]['datatype'] == 'bool':
                                    new_define = {};
                                    #new_define['boolean'] = True
                                    new_define['name'] = param
                                    if eda_yaml['parameters'][param]['default'] == True:
                                        new_define['value'] = 1
                                    else:
                                        new_define['value'] = 0
                                    defines.append(new_define)
                                else:
                                    print("Support for non-bool FuseSoC parameters is not currently implemented")
                            
                            for option in eda_yaml['tool_options']['xsim']['xelab_options']:
                                if (re.match("--define", option)):
                                    new_define = {};
                                    matches = re.search("--define\s+(\w+)\s*(?:=\s*(\S+))?", option)
                                    if matches:
                                        new_define['name'] = matches.group(1)
                                        if len(matches.groups()) > 2:
                                            new_define['value'] = matches.group(2)
                                        else:
                                            new_define['boolean'] = True
                                        defines.append(new_define)
                            
                            flist_template = cfg.templateEnv.get_template("vivado.flist.j2")
                            outputText = flist_template.render(defines=defines, files=files, dirs=dirs)
                            vlog_flist_file_path = eda_file_dir + "/" + file_path_partial_name + "_0.flist"
                            with open(vlog_flist_file_path,'w') as flist_file:
                                flist_file.write(outputText)
                            flist_file.close()
                            
                            print("\033[1;35m*************")
                            print("Compiling RTL")
                            print("*************\033[0m")
                            vlog_compilation_log_path = cfg.pwd + "/results/" + rtl_ip_name + ".xvlog.cmp.log"
                            vivado.run_bin("xvlog", " --incr --relax -sv -f " + vlog_flist_file_path + " " + args + " --log " + vlog_compilation_log_path + " --work " + rtl_ip_name + "=./out/" + rtl_ip_name)
                            add_cmp_to_history_log(rtl_ip_name + ".xvlog", vlog_compilation_log_path)
                else:
                    print("ERROR: Could not find output '.eda.yml' file from FuseSoC")
                
                
            else:
                print("ERROR: Could not find FuseSoC DUT IP core file for " + rtl_ip_name)




def cmp_dv(ip_name, args):
    with open(discovery.ip_paths[ip_name] + "/ip.yml", 'r') as yamlfile:
        dv_yaml = yaml.load(yamlfile, Loader=SafeLoader)
        if dv_yaml:
            # TODO Add Support for simulators other than Vivado
            filelist_path = discovery.ip_paths[ip_name] + "/" + dv_yaml['structure']['src-path'] + "/" + dv_yaml['hdl-src']['flist']['vivado']
        do_cmp_dv(filelist_path, ip_name, args)




def do_cmp_dv(filelist_path, lib_name, args):
    if (cfg.dbg):
        print("Call to do_cmp_dv(filelist_path='" + filelist_path + "', lib_name='" + lib_name + "')")
    print("\033[0;36m************")
    print("Compiling DV")
    print("************\033[0m")
    if not os.path.exists(cfg.sim_results_dir):
        os.mkdir(cfg.sim_results_dir)
    compilation_log_path = cfg.sim_results_dir + "/" + lib_name + ".cmp.log"
    add_cmp_to_history_log(lib_name, compilation_log_path)
    vivado.run_bin("xvlog", "--incr -sv -f " + filelist_path + " " + args + " -L uvm --work " + lib_name + "=./out/" + lib_name + " --log " + compilation_log_path)
