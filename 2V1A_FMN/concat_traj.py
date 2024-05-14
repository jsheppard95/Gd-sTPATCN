"""
Script to concate *.xtc trajectories
"""

import subprocess

dirs = ["07NPT_200-250ns", "08NPT_250-300ns", "09NPT_300-350ns",
        "10NPT_350-400ns", "11NPT_400-450ns", "12NPT_450-500ns"]

cmd = "gmx_mpi trjcat -f "
for d in dirs:
    cmd += f"{d}/npt_pbc.xtc "

cmd += "-o full_trajec/npt_pbc_200-500ns.xtc"
subprocess.call(cmd, shell=True)