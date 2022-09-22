#!/bin/bash
#This for full run of the ABX pipeline in command line


#AESRC corpus
declare -a accents=("American" "Japanese" "British" "Canadian" "Chinese" "Indian" "Korean" "Spanish" "Portuguese" "Russian")

#parametres
results= $1
abx="/abx"
item_file="/item_file.item"
phone="/abx_file.abx"#file is eather within or across
distance_file="/distance.distance"
score_file="/score.score"
analyse_file="/task.csv"
features_file="/h5_file.h5f"

for accent in ${accents[@]};do
    output="$results$accent$abx";

    #item_file
    item="$output$item_file";
    task="$output$phone";
    distance="$output$distance_file";
    features="$output$features_file";

    # computing distances
    abx-distance $features $task $distance --normalization 1
done

