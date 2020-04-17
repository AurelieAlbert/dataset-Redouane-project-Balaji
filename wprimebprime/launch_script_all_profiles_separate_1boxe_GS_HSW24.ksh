#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --threads-per-core=1
#SBATCH --constraint=HSW24
#SBATCH -J wbprime
#SBATCH -e wbprime.e%j
#SBATCH -o wbprime.o%j
#SBATCH --time=23:00:00
#SBATCH --exclusive


date='20090702'

set -x
ulimit -s
ulimit -s unlimited

export PATH="/scratch/cnt0024/hmg2840/albert7a/anaconda3/bin:$PATH"
k=3
python compute-wprime-bprime-separate-files-per-profile.py 'GS' $k $date > output_compute-wprimebprime-boxes-GS-box-$3-${date}_HSW24.txt 



