#!/bin/bash
#
# This is for the ABX task "On Phone" used for the AESRC corpus
#

##### AESRC Corpus #####
#         American	#
#         British	#
#         Canadian	#
#         Chinese	#
#         Indian        #
#         Japanese	#
#         Korean        #
#         Spanish	#
#	Portuguese	#
#          Russian	#
#########################

echo "$(hostname)"

#AESRC corpus
#declare -a accents=("British" "Canadian" "Chinese" "Indian" "Japanese" "Korean" "Spanish" "Portuguese" "Russian")
declare -a accents=("Spanish" "Japanese" "Portuguese")


#parametres
results="/scratch2/mkhentout/AESRC_2H/results/test/"
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

    echo "spec= $task_spec";echo -e "\n";
    which abx-task
    abx-task $item $task_1 $task_spec -v

done
