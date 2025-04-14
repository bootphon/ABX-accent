#!/bin/bash
#
# AESRC corpus ABX task analysis script
#
#SBATCH --partition=gpu
#SBATCH --nodelist=your-node-name

# Loading modules and activating the right conda environment
source #your_source  # TODO: Replace with your actual source path
module load espeak
conda activate abx

# Define accents to process
declare -a accents=("American" "Japanese" "British" "Canadian" "Chinese" "Indian" "Korean" "Spanish" "Portuguese" "Russian")

# Parameters
results=$1  # First argument should be the base results directory

# Define path suffixes
abx="/abx"
item_file="/item_file.item"
phone="/abx_file.abx"  # file is either within or across
distance_file="/distance.distance"
score_file="/score.score"
analyse_file="/task.csv"
features_file="/h5_file.h5f"

# Process each accent
for accent in "${accents[@]}"; do
    echo "Processing $accent accent..."
    
    # Define output paths
    output="${results}${accent}${abx}"
    item="${output}${item_file}"
    task="${output}${phone}"
    analyze="${output}${analyse_file}"
    features="${results}${accent}${features_file}"
    
    # Check if output directory exists
    if [ ! -d "$output" ]; then
        echo "Creating directory: $output"
        mkdir -p "$output"
    fi
    
    # Check if required files exist
    if [ ! -f "$task" ]; then
        echo "Error: Task file $task does not exist!"
        continue
    fi
    
    if [ ! -f "$score_file" ]; then
        echo "Error: Score file not found: $score_file"
        continue
    fi
    
    # Analyze the results
    echo "Analyzing ABX results for $accent..."
    abx-analyze "$score_file" "$task" "$analyze"
    
    echo "Completed processing for $accent"
done

echo "All accents processed successfully."
