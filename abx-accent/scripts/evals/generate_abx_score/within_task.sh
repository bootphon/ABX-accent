#!/bin/bash
#
# ABX Within-Speaker Task Creation Script for AESRC Corpus
#
#SBATCH --partition=gpu
#SBATCH --nodelist=your-node-name

# Loading modules and activating the right conda environment
source #your_source  # TODO: Replace with your actual source path
module load espeak
conda activate abx

# Define accents to process
declare -a accents=("American" "British" "Canadian" "Chinese" "Indian" "Japanese" "Korean" "Spanish" "Portuguese" "Russian")

# Parameters
results=$1  # First argument should be the base results directory

# Define path suffixes and task specifications
abx="/abx"
task_spec="-o phone -b speaker prev-phone next-phone"  # Within-speaker task specification
item_file="/item_file.item"
phone="/abx_within.abx"  # Output file for within-speaker ABX task

# Check if results directory was provided
if [ -z "$results" ]; then
    echo "Error: No results directory specified"
    echo "Usage: $0 <results_directory>"
    exit 1
fi

# Display which abx-task executable will be used
which abx-task

# Process each accent
echo "Starting ABX within-speaker task creation for all accents..."

for accent in "${accents[@]}"; do
    echo "Processing $accent accent..."
    
    # Define output paths
    output="${results}${accent}${abx}"
    item="${output}${item_file}"
    task="${output}${phone}"
    
    # Check if item file exists
    if [ ! -f "$item" ]; then
        echo "Error: Item file not found: $item"
        continue
    fi
    
    # Check if output directory exists
    if [ ! -d "$(dirname "$task")" ]; then
        echo "Creating directory: $(dirname "$task")"
        mkdir -p "$(dirname "$task")"
    fi
    
    # Create ABX task
    echo "Creating within-speaker ABX task for $accent..."
    abx-task "$item" "$task" $task_spec -v
    
    if [ $? -eq 0 ]; then
        echo "Within-speaker task creation completed successfully for $accent"
    else
        echo "Error: Within-speaker task creation failed for $accent"
    fi
done

echo "ABX within-speaker task creation complete for all accents."
