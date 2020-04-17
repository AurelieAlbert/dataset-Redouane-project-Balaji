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


date='20090703'

set -x
ulimit -s
ulimit -s unlimited

export PATH="/scratch/cnt0024/hmg2840/albert7a/anaconda3/bin:$PATH"
k=1
python compute-wprime-bprime-mean.py 'GS' $k $date > output_compute-wprimebprime-boxes-GS-box-$k-${date}_VISU.txt 



