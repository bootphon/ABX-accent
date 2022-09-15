#!/bin/bash
#
# This is for the ABX task "On Phone" used for the AESRC corpus
#


#AESRC corpus
declare -a accents=("American" "British" "Canadian" "Chinese" "Indian" "Japanese" "Korean" "Spanish" "Portuguese" "Russian")

#parametres
results=$1
abx="/abx"
task_spec="-o phone -b speaker prev-phone next-phone"
item_file="/item_file.item"
phone="/abx_task1.abx"

for accent in ${accents[@]};do

    output="$results$accent$abx";
    #item_file
    item="$output$item_file";
    #task
    task_1="$output$phone";
    
    which abx-task
    abx-task $item $task_1 $task_spec -v

done
