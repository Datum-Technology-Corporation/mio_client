# Copyright Datum Technology Corporation
########################################################################################################################
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
########################################################################################################################


setup(
    name="mio",
    packages=["mio"],
    use_scm_version={
        "relative_to": __file__,
        "write_to": "mio/version.py",
    },
    author="Datum Technology Corporation",
    author_email="contact@datumtc.ca",
    description=(
        "Moore.io (MIO) is a Front-End Hardware Development Toolchain and IP Catalog for ASIC/FPGA engineering."
    ),
    license="Apache-2.0 WITH SHL-2.1",
    keywords=[
        "SystemVerilog",
        "UVM",
        "DV",
        "verilog",
        "VHDL",
        "hdl",
        "rtl",
        "synthesis",
        "FPGA",
        "simulation",
        "Xilinx",
        "Altera"
    ],
    url="https://github.com/Datum-Technology-Corporation/mio_cli",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Topic :: Utilities",
        "Topic :: Software Development :: Build Tools"
    ],
    entry_points={"console_scripts": ["mio = mio.__main__:main"]},
    setup_requires=[
        "setuptools_scm",
    ],
    install_requires=[
        "docopt",
        "fusesoc"
    ],
    # Supported Python versions: 3.6+
    python_requires=">=3.6, <4",
)
