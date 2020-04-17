#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --threads-per-core=1
#SBATCH --constraint=BDW28
#SBATCH -J boxGS
#SBATCH -e boxGS.e%j
#SBATCH -o boxGS.o%j
#SBATCH --time=02:30:00
#SBATCH --exclusive


date='20090701'

set -x
ulimit -s
ulimit -s unlimited

export PATH="/scratch/cnt0024/hmg2840/albert7a/anaconda3/bin:$PATH"
python compute-wprime-bprime.py 'GS' 1 $date > output_compute-wprimebprime-boxes-GS-box-${km}-${date}_BDW28.txt



