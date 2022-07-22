# Copyright 2022 Datum Technology Corporation
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
########################################################################################################################

from setuptools import find_packages, setup

setup(
    install_requires=['docopt','jinja2','fusesoc','toml','requests'],
    # other arguments here...
    entry_points={
        'console_scripts': [
            'mio = mio.__main__:main'
        ]
    }
)
