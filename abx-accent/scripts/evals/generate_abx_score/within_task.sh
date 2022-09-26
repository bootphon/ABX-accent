#!/bin/bash
#SBATCH --partition=gpu
#SBATCH --nodelist=puck5

# loading modules and activating the right conda env
source #your_source
module load espeak
conda activate abx


#AESRC corpus
declare -a accents=("American" "British" "Canadian" "Chinese" "Indian" "Japanese" "Korean" "Spanish" "Portuguese" "Russian")

#parametres
results=$1
abx="/abx"
task_spec="-o phone -b speaker prev-phone next-phone"
item_file="/item_file.item"
phone="/abx_within.abx"

for accent in ${accents[@]};do

    output="$results$accent$abx";
    #item_file
    item="$output$item_file";
    #task
    task="$output$phone";
    
    which abx-task
    abx-task $item $task $task_spec -v

done
