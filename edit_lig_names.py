"""
edit_lig_names.py

Modifies ligand names from CHARMM-GUI FF Converter to remove conflict between
ligand and protein force field parameters.
"""

import os

# Get LIG.itp filename
lig_infile = os.path.join("2V1A_FMN", "charmm-gui-FF-convert", "gromacs", "toppar", "LIG.itp")
lig_outfile = os.path.join("2V1A_FMN", "charmm-gui-FF-convert", "gromacs", "toppar", "LIG_processed.itp")

# Append `_` to `type` in `[ atoms ]` section
# e.g `OG2D3` -> `OG2D3_`

N_ATOMS = 52

with open(lig_infile, "r") as fin:
    with open(lig_outfile, "w") as fout:
        # Read until `[ atoms ]`` section
        while True:
            line = fin.readline()
            if not line:
                break
            if line == "[ atoms ]\n":
                fout.write(line)
                line = fin.readline()  # comment line
                fout.write(line)
                for i in range(N_ATOMS):
                    line = fin.readline()
                    data = line.split()
                    for i in range(len(data)):
                        if i == 1:
                            # `type` entry
                            fout.write("     " + data[i] + "_")
                        else:
                            fout.write("     " + data[i])
                    fout.write("\n")
            else:
                fout.write(line)

