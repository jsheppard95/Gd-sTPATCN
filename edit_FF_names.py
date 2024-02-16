"""
edit_FF_names.py

Modifies ligand atom type names in force field parameter file to remove
conflict between ligand and protein force field parameters
"""

import os
# Get forcefield.itp filename
ff_infile = os.path.join("2V1A_FMN", "charmm-gui-FF-convert", "gromacs", "toppar", "forcefield.itp")
ff_outfile = os.path.join("2V1A_FMN", "charmm-gui-FF-convert", "gromacs", "toppar", "forcefield_processed.itp")

# Append `_` to a `name` entries in:
# [ atomtypes ]
# [ bondtypes ]
# [ pairtypes ]
# [ angletypes ]
# [ dihedraltypes ]
# [ dihedraltypes ]
sections = ["[ atomtypes ]", "[ bondtypes ]", "[ pairtypes ]", "[ angletypes ]", "[ dihedraltypes ]"]
with open(ff_infile, "r") as fin:
    with open(ff_outfile, "w") as fout:
        while True:
            line = fin.readline()
            if not line:
                break
            data = line.split()
            if line != "\n":
                if data[0].isupper():  # Identify rows containing atoms
                    for i in range(len(data)):
                        if data[i].isupper() and i < 4:
                            fout.write("    " + data[i] + "_")
                        else:
                            fout.write("    " + data[i])
                    fout.write("\n")
            
                else:
                    fout.write(line)
            else:
                fout.write(line)