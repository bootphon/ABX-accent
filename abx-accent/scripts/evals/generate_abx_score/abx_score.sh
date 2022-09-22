#!/bin/bash
#This for full run of the ABX pipeline in command line


#AESRC corpus
declare -a accents=("American" "Japanese" "British" "Canadian" "Chinese" "Indian" "Korean" "Spanish" "Portuguese" "Russian")

#parametres
results= $1
abx="/abx"
item_file="/item_file.item"
phone="/abx_task1.abx"
distance_file="/distance1.distance"
score_file="/score.score"
analyse_file="/task.csv"
features_file="/h5_file.h5f"

for accent in ${accents[@]};do
    output="$results$accent$abx";

    #item_file
    item="$output$item_file";
    task="$output$phone";
    score="$output$score_file";
    features="$output$features_file";

    # calculating the score
    abx-score $task $distance $score

    

done
