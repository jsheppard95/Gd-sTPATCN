#!/bin/bash

#SBATCH -J protein_npt           # Job name
#SBATCH -o npt.o%j       # Name of stdout output file
#SBATCH -e npt.e%j       # Name of stderr error file
#SBATCH -p normal          # Queue (partition) name
#SBATCH -N 1               # Total # of nodes (must be 1 for serial)
#SBATCH -n 64               # Total # of mpi tasks (should be 1 for serial)
#SBATCH -t 04:00:00        # Run time (hh:mm:ss)
#SBATCH --mail-user=lobo@ucsb.edu
#SBATCH --mail-type=all    # Send email at begin and end of job
#SBATCH -A TG-MCA05S027       # Allocation name (req'd if you have more than 1)

# Other commands must follow all #SBATCH directives...

module load intel/18.0.2                                                           
module load impi/18.0.2                                                            
module load boost                                                                  
module load gromacs/2019.6 

module list
pwd
date

# Launch serial code...


ibrun -np 64 mdrun_mpi_knl -deffnm npt -v -cpi >& mdjob

# ---------------------------------------------------
