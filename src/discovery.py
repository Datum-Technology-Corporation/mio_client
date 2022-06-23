# Copyright Datum Technology Corporation
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
########################################################################################################################


import cfg
import clean
import cmp
import cov
import dox
import elab
import history
import results
import vivado

import os
import toml
from datetime import datetime
import yaml
from yaml.loader import SafeLoader
import collections


project_toml_file_path = "../mio.toml"
ip_paths      = {}
ip_metadata   = {}


def find_project_toml_file():
    found_file = False
    current_dir = cfg.pwd
    while found_file == False:
        if not os.path.exists(current_dir):
            sys.exit("Failed to find Moore.io project TOML Configuration file.  Exiting.")
        else:
            project_toml_file_path = os.path.join(current_dir, "mio.toml")
            if not os.path.exists(project_toml_file_path):
                current_dir = os.path.join(current_dir, "..")
            else:
                found_file = True
                cfg.project_dir = current_dir
                if cfg.dbg:
                    print("Found Moore.io project TOML Configuration file at " + project_toml_file_path)


def load_configuration():
    builtin_toml_file_path = os.path.join(cfg.mio_client_dir, "bin/mio.toml")
    user_toml_file_path = os.path.join(cfg.user_dir, "mio.toml")
    
    cfg.configuration = toml.load(builtin_toml_file_path)
    if os.path.exists(user_toml_file_path):
        merge_dict(cfg.configuration, toml.load(user_toml_file_path))
        if cfg.dbg:
            print("Found Moore.io user TOML Configuration file at " + user_toml_file_path)
    merge_dict(cfg.configuration, toml.load(project_toml_file_path))
    print("Final configuration:\n" + toml.dumps(cfg.configuration))
    
    cfg.project_name      = cfg.configuration.get("project", {}).get("name")
    cfg.sim_dir           = os.path.join(cfg.project_dir, cfg.configuration.get("simulation", {}).get("root-path"))
    cfg.sim_results_dir   = os.path.join(cfg.sim_dir    , cfg.configuration.get("simulation", {}).get("results-dir"))
    cfg.history_file_path = os.path.join(cfg.sim_dir    , cfg.configuration.get("simulation", {}).get("history-filename"))
    cfg.sim_output_dir    = os.path.join(cfg.sim_dir    , cfg.configuration.get("simulation", {}).get("output-dir"))
    cfg.ip_paths          = cfg.configuration.get("ip", {}).get("paths")
    cfg.test_results_path_template = cfg.configuration.get("simulation", {}).get("test-result-path-template")


def catalog_ips():
    for ip_path in cfg.ip_paths:
        full_ip_path = os.path.join(cfg.project_dir, ip_path)
        search_dir_for_ip(full_ip_path)
    search_dir_for_ip(cfg.dependencies_path)


def search_dir_for_ip(path):
    if os.path.exists(path):
        if cfg.dbg:
            print("Searching " + path + " for IP")
        for dirpath, dirnames, filenames in os.walk(path):
            for dir in dirnames:
                current_dir_path    = os.path.join(path            , dir)
                current_ip_yml_path = os.path.join(current_dir_path, "ip.yml")
                if os.path.exists(current_ip_yml_path):
                    ip_paths[dir] = current_dir_path
                    if cfg.dbg:
                        print("Found IP! name='" + dir + "', path='" + current_dir_path + "'")
                    with open(current_ip_yml_path, 'r') as yamlfile:
                        ip_yaml = yaml.load(yamlfile, Loader=SafeLoader)
                        if ip_yaml:
                            ip_name = ip_yaml["ip"]["name"]
                            ip_metadata[ip_name] = ip_yaml


def set_env_vars():
    for ip in ip_metadata:
        env_var_name = ip_metadata[ip]["ip"]["type"] + "_" + ip_metadata[ip]["ip"]["name"] + "_SRC_PATH"
        env_var_name = env_var_name.upper()
        ip_src_path = os.path.join(ip_paths[ip], ip_metadata[ip]["structure"]["src-path"])
        os.environ[env_var_name] = ip_src_path


def merge_dict(d1, d2):
    """
    Modifies d1 in-place to contain values from d2.  If any value
    in d1 is a dictionary (or dict-like), *and* the corresponding
    value in d2 is also a dictionary, then merge them in-place.
    """
    for k, v2 in d2.items():
        v1 = d1.get(k)  # returns None if v1 has no value for this key
        if (isinstance(v1, collections.Mapping) and
                isinstance(v2, collections.Mapping)):
            merge_dict(v1, v2)
        else:
            d1[k] = v2
