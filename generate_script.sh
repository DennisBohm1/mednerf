#!/bin/sh

#SBATCH --job-name=generate_ct_scan
#SBATCH --partition=gpu
#SBATCH --account=Education-EEMCS-MSc-CS
#SBATCH --time=00:30:00
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=1
#SBATCH --gpus-per-task=1
#SBATCH --mem-per-cpu=1GB

module load 2022r2
module load openmpi
module load python
module load py-matplotlib
module load py-numpy
module load py-pyyaml
module load py-pillow
module load py-torch
module load py-setuptools
module load py-scipy
module load py-scikit-learn
module load py-pip
module load cuda/11.6
module load py-tqdm
srun python graf-main/render_xray_G_Z.py > output.log