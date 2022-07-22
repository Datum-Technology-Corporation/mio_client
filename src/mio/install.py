# Copyright 2022 Datum Technology Corporation
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
########################################################################################################################
import yaml
from yaml import SafeLoader

import mio.cfg
import mio.discovery

import requests
import getpass
import tarfile
import json
from pathlib import Path
from base64 import b64decode
import os
import shutil


base_url          = "https://mooreio.org"#"http://localhost:8080"
jwt_endpoint      = base_url + "/api/authenticate"
ips_endpoint      = base_url + "/api/ips"
versions_endpoint = base_url + "/api/versions"
version_endpoint  = base_url + "/api/version/"
licenses_endpoint = base_url + "/api/licenses"
headers = {}


def install_mio_ip(name, location):
    query = {'name': name}
    response = requests.get(ips_endpoint, params=query, headers=headers)
    json_data = response.json()
    payload = None
    found_payload = False
    for ip in json_data:
        if ip['name'] == name:
            ip_id = ip['id']
            print("Found IP! name=" + name + " id=" + str(ip_id))
            license_type = ip['licenseType']
            if license_type == "PUBLIC_OPEN_SOURCE":
                versions = requests.get(versions_endpoint, headers=headers).json()
                for version in versions:
                    if version['ip']['id'] == ip_id:
                        print("Found IP version on server: " + name + " v" + version['semver'])
                        payload = version['publicPayload']
                        found_payload = True
                        break
            if license_type == "PUBLIC_ENCRYPTED":
                licenses = requests.get(licenses_endpoint, headers=headers).json()
                for license in licenses:
                    if license['targetIp']['id'] == ip_id:
                        print("Found IP license on server: " + name)
                        payload = license['payload']
                        found_payload = True
                        break
    if found_payload:
        filename = Path(location + "/" + name + '.tgz')
        filename.write_bytes(b64decode(payload))
        tar = tarfile.open(filename, "r:gz")
        ip_destination_path = location + "/" + name
        if os.path.exists(ip_destination_path):
            shutil.rmtree(ip_destination_path)
        os.mkdir(ip_destination_path)
        tar.extractall(ip_destination_path)
        tar.close()
        os.remove(filename)
    else:
        print("ERROR: Could not find IP '" + name + "' on Moore.io server")



def login(username, password):
    global headers
    if username == None or username == "":
        username = input("Please enter your Moore.io account username: ")
    if password == None or password == "":
        password = getpass.getpass(prompt='Password: ')
    payload = {
        "username": username,
        "password": password,
        "rememberMe": "true"
    }
    jwt_token_response= requests.post(jwt_endpoint, json=payload)
    #print(jwt_token_response.json())
    #print(jwt_token_response.json()['id_token'])
    headers={'Authorization':'Bearer '+jwt_token_response.json()['id_token']}


def get_ips_for_target(ip_name):
    dependencies = []
    ip_metadata = discovery.ip_metadata[ip_name]
    if 'dependencies' in ip_metadata:
        for dependency in ip_metadata['dependencies']:
            dependencies.append(dependency['name'])
    else:
        print("ERROR: no dependencies section in " + ip_name + "'s ip.yml")
    return dependencies


def install_mio_ips(name, ip_list, location, username, password):
    if ip_list == None:
        print("No dependencies were found in " + name + "'s ip.yml")
    else:
        login(username, password)
        for ip in ip_list:
            install_mio_ip(ip, location)


def install_all_ips_for_target(target_name, global_install, username, password):
    ip_list = get_ips_for_target(target_name)
    
    if global_install:
        location = cfg.user_global_ips_path
    else:
        location = cfg.dependencies_path
    if not os.path.exists(cfg.mio_data_dir):
        os.mkdir(cfg.mio_data_dir)
    if not os.path.exists(location):
        os.mkdir(location)
    install_mio_ips(target_name, ip_list, location, username, password)
