#!/bin/bash  -l

#the -l is needed on first line if you want to use modules

#SBATCH -J 2V1A_implicit_solv_4kbar_Restart   # Job name
#SBATCH -o output  
#SBATCH -e error  
#SBATCH --nodes=1 --ntasks-per-node 40
#SBATCH --mail-user=sheppard@ucsb.edu
#SBATCH --mail-type=all
#SBATCH -t 800:00:00  


module load intel/18
source /sw/chem/amber20/amber.sh
source /home/jsheppard/bin/plumed-2.9.0/sourceme.sh


cd $SLURM_SUBMIT_DIR

/bin/hostname

mpirun -np $SLURM_NPROCS pmemd.MPI -O -i sim.in -o 2v1a-MD.out -c 2v1a-MD.ncrst -p 2v1a.prmtop -r 2v1a-MD.ncrst -x 2v1a-MD.nc > logfile
