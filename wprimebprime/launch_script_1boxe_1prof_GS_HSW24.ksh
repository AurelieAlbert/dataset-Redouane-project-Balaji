#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --threads-per-core=1
#SBATCH --constraint=HSW24
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
k=5
tt=0
yt=0
xt=0
python compute-wprime-bprime-one-profile.py 'GS' $k $date $tt $yt $xt  > output_compute-wprimebprime-boxes-GS-box-$k-$tt-$yt-$xt-${date}_HSW24.txt 



