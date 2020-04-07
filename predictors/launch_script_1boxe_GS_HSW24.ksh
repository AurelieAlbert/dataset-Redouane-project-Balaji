#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --threads-per-core=1
#SBATCH --constraint=HSW24
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
python extractions-gradients-all-variables-boxes.py 'GS' 2 $date > output_extractions-gradients-all-variables-boxes-GS-box-${km}-${date}_HSW24.txt 



