#!/bin/bash
# Script to run convert_features.py for multiple accents

# Base directories
BASE_DIR="your-path"
OUTPUT_FEATURES_DIR="./features"
OUTPUT_TIMES_DIR="./times"

# List of all accents to process
declare -a ACCENTS=(
  "American"
  "British"
  "Indian"
  "Chinese"
  "Japanese"
  "Korean"
  "Russian"
  "Spanish"
  "Portuguese"
)

# Create output directories if they don't exist
mkdir -p "$OUTPUT_FEATURES_DIR"
mkdir -p "$OUTPUT_TIMES_DIR"

# Loop through each accent and run the conversion
for accent in "${ACCENTS[@]}"; do
  echo "======================================================"
  echo "Processing accent: $accent"
  echo "======================================================"
  
  # Construct the input file path
  H5_FILE="$BASE_DIR/results/dev/$accent/abx/h5_file.h5f"
  
  # Create accent-specific output directories
  accent_features_dir="$OUTPUT_FEATURES_DIR/$accent"
  accent_times_dir="$OUTPUT_TIMES_DIR/$accent"
  
  mkdir -p "$accent_features_dir"
  mkdir -p "$accent_times_dir"
  
  # Run the conversion
  echo "Running: uv run convert_features.py torch $H5_FILE $accent_features_dir $accent_times_dir"
  uv run convert_features.py torch "$H5_FILE" "$accent_features_dir" "$accent_times_dir"
  
  # Check if the command was successful
  if [ $? -eq 0 ]; then
    echo "Conversion completed successfully for $accent"
  else
    echo "Error: Conversion failed for $accent"
  fi
  
  echo ""
done

echo "All accents have been processed."
