#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --threads-per-core=1
#SBATCH --constraint=VISU
#SBATCH -J wbprime
#SBATCH -e wbprime.e%j
#SBATCH -o wbprime.o%j
#SBATCH --time=06:00:00
#SBATCH --exclusive


date='20090701'

set -x
ulimit -s
ulimit -s unlimited

export PATH="/scratch/cnt0024/hmg2840/albert7a/anaconda3/bin:$PATH"
python compute-wprime-bprime-separate-files-per-profile.py 'GS' 2 $date > output_compute-wprimebprime-boxes-GS-box-2-${date}_VISU.txt 



