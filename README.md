# 2DL4NLP
UvA DL4NLP mini-project

First, clone the JoeyNMT (https://github.com/joeynmt/joeynmt) and the 2DL4NLP gits into the same folder.

To run a model for the pretraining task, run:
srun python -u -m joeynmt train /code/configs/FINAL_XX.yaml
For XX input a language code (el, el_r, ru, ru_r, ja, ja_r, th, th_r, pl)

To run a model for the transfer learning task, run:
srun python -u -m joeynmt train /code/configs/FINAL_pre_XX.yaml
For XX input a language code (el, el_r, ru, ru_r, ja, ja_r, th, th_r, pl)

To run a model on LISA using batch files, use one of the batch files in /code (jobbert_FINAL_XX.sh or jobbert_FINAL_pre_XX.sh)

For the transfer learning task, the checkpoint files of the pretraining task must be modified using the pl_INIT checkpoint file:
1) Run: srun python -u -m joeynmt train /code/configs/FINAL_pl_INIT.yaml (this creates the pl_INIT checkpoint)
2) Run the adjust_checkpoints notebook (first create a folder "checkpoints", with a folder "checkpoints_adjusted" in it, for the script to run properly.)
3) Save the checkpoints file in the same folder as the gits, in a folder named "checkpoints".
