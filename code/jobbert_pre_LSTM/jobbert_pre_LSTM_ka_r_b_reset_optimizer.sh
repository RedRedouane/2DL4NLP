#!/bin/bash

#SBATCH --partition=gpu_shared_course
#SBATCH --gres=gpu:1
#SBATCH --job-name=pre_LSTM_ka_r_b_reset_optimizer
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --time=24:00:00
#SBATCH --mem=32000M
#SBATCH --output=pre_LSTM_ka_r_b_reset_optimizer.out

module purge
module load 2019
module load Python/3.7.5-foss-2019b
module load CUDA/10.1.243
module load cuDNN/7.6.5.32-CUDA-10.1.243
module load NCCL/2.5.6-CUDA-10.1.243
module load Anaconda3/2018.12

# Your job starts in the directory where you call sbatch
cd $HOME/joeynmt/
# Activate your environment
# source $HOME/joeynmt/jnmt/bin/activate
# Run your code
srun python -u -m joeynmt train ../2DL4NLP/code/configs/pre_LSTM_ka_r_b_reset_optimizer.yaml
