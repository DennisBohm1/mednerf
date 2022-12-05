#!/bin/sh

#SBATCH --job-name=generate_ct_scan
#SBATCH --partition=compute
#SBATCH --account=Education-EEMCS-MSc-CS
#SBATCH --time=00:30:00
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2GB

module load 2022r2
module load openmpi
module load python
module load py-numpy
srun python graf-main/render_xray_G_Z.py > output.log