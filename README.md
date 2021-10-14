# 2DL4NLP
UvA DL4NLP mini-project

To run a model for the pretraining task, run:
srun python -u -m joeynmt train /code/configs/FINAL_XX.yaml
For XX input a language code (el, el_r, ru, ru_r, ja, ja_r, th, th_r, pl)

To run a model for the transfer learning task, run:
srun python -u -m joeynmt train /code/configs/FINAL_pre_XX.yaml
For XX input a language code (el, el_r, ru, ru_r, ja, ja_r, th, th_r, pl)

To run a model on LISA using batch files, use one of the batch files in /code (jobbert_FINAL_XX.sh or jobbert_FINAL_pre_XX.sh)
