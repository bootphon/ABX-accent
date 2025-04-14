#!/bin/bash
#
# This script runs the distance calculation step of the ABX pipeline
# for the AESRC corpus across multiple accents
#

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

# Check if results directory was provided
if [ -z "$results" ]; then
    echo "Error: No results directory specified"
    echo "Usage: $0 <results_directory>"
    exit 1
fi

# Process each accent
echo "Starting ABX distance calculation for all accents..."

for accent in "${accents[@]}"; do
    echo "Processing $accent accent..."
    
    # Define output paths
    output="${results}${accent}${abx}"
    item="${output}${item_file}"
    task="${output}${phone}"
    distance="${output}${distance_file}"
    features="${results}${accent}${features_file}"
    
    # Check if required files exist
    if [ ! -f "$features" ]; then
        echo "Error: Features file not found: $features"
        continue
    fi
    
    if [ ! -f "$task" ]; then
        echo "Error: Task file not found: $task"
        continue
    fi
    
    # Check if output directory exists
    if [ ! -d "$(dirname "$distance")" ]; then
        echo "Creating directory: $(dirname "$distance")"
        mkdir -p "$(dirname "$distance")"
    fi
    
    # Computing distances
    echo "Computing distances for $accent..."
    abx-distance "$features" "$task" "$distance" --normalization 1
    
    if [ $? -eq 0 ]; then
        echo "Distance calculation completed successfully for $accent"
    else
        echo "Error: Distance calculation failed for $accent"
    fi
done

echo "ABX distance calculation complete for all accents."
