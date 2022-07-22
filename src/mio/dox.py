# Copyright 2022 Datum Technology Corporation
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
########################################################################################################################


import subprocess
import mio.discovery
import mio.cfg


def gen_doxygen(ip_name):
    if ip_name not in discovery.ip_paths:
        sys.exit("Failed to find IP '" + ip_name + "'.  Exiting.")
    ip_path = discovery.ip_paths[ip_name]
    ip_metadata = discovery.ip_metadata[ip_name]
    ip_src_path = ip_path + "/" + ip_metadata['structure']['src-path']
    ip_bin_path = ip_path + "/" + ip_metadata['structure']['scripts-path']
    args = "SRC_PATH=" + ip_src_path + " MIO_HOME=" + cfg.mio_client_dir + " IP_NAME=" + ip_name
    subprocess.call(args + " doxygen " + ip_bin_path + "/doxygen.cfg", shell=True)
