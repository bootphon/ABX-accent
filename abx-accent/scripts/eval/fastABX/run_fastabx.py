#!/usr/bin/env python
# /// script
# requires-python = "==3.12"
# dependencies = [
#    "fastabx>=0.2.0"
# ]
# ///

"""
ABX Task Processor for AESRC Accent Data

This script processes ABX (Audio by eXample) tasks for different accents
using the fastabx library. It computes discrimination scores for phone
discrimination tasks across speakers within each accent.
"""

import os
import sys
from pathlib import Path
from typing import List

try:
    from fastabx import Dataset, Task, Score
except ImportError as e:
    print(f"Error: Failed to import fastabx: {e}")
    print("Please ensure fastabx>=0.2.0 is installed.")
    sys.exit(1)


class ABXProcessor:
    """Processes ABX tasks for different accents."""
    
    def __init__(self, base_dir: str, features_dir: str, times_dir: str):
        """
        Initialize the ABX processor.
        
        Args:
            base_dir: Base directory containing item files
            features_dir: Directory containing feature files
            times_dir: Directory containing timing files
        """
        self.base_dir = Path(base_dir)
        self.features_dir = Path(features_dir)
        self.times_dir = Path(times_dir)
        
        # Create output directories if they don't exist
        self.features_dir.mkdir(parents=True, exist_ok=True)
        self.times_dir.mkdir(parents=True, exist_ok=True)
    
    def get_item_file_path(self, accent: str) -> Path:
        """
        Get the path to the item file for a given accent.
        
        Args:
            accent: Name of the accent
            
        Returns:
            Path to the item file
        """
        return self.base_dir / accent / "abx" / f"{accent.lower()}_item.item"
    
    def get_accent_directories(self, accent: str) -> tuple[Path, Path]:
        """
        Get accent-specific feature and times directories.
        
        Args:
            accent: Name of the accent
            
        Returns:
            Tuple of (features_dir, times_dir) for the accent
        """
        accent_features = self.features_dir / accent
        accent_times = self.times_dir / accent
        
        # Use accent-specific directories if they exist, otherwise use base directories
        features_dir = accent_features if accent_features.exists() else self.features_dir
        times_dir = accent_times if accent_times.exists() else self.times_dir
        
        return features_dir, times_dir
    
    def process_accent(self, accent: str) -> bool:
        """
        Process ABX tasks (both across and within) for a single accent.
        
        Args:
            accent: Name of the accent to process
            
        Returns:
            True if successful, False otherwise
        """
        print(f"{'='*60}")
        print(f"Processing accent: {accent}")
        print(f"{'='*60}")
        
        # Get paths
        item_file = self.get_item_file_path(accent)
        features_dir, times_dir = self.get_accent_directories(accent)
        
        # Check if item file exists
        if not item_file.exists():
            print(f"Warning: Item file not found: {item_file}")
            print(f"Skipping {accent}")
            return False
        
        try:
            # Load dataset
            print(f"Loading dataset from {item_file}")
            print(f"Features directory: {features_dir}")
            print(f"Times directory: {times_dir}")
            
            dataset = Dataset.from_item_with_times(
                str(item_file),
                str(features_dir),
                str(times_dir)
            )
            
            # Process ACROSS task
            print("Creating across-speaker task")
            across_output_csv = f"{accent.lower()}_dev_across_scores.csv"
            across_task = Task(
                dataset,
                on="#phone",
                by=["next-phone", "prev-phone"],
                across=["speaker"]
            )
            
            print("Computing across-speaker scores with angular distance")
            across_score = Score(across_task, "angular")
            
            print(f"Writing across-speaker results to {across_output_csv}")
            across_score.write_csv(across_output_csv)
            
            print("Across-speaker collapsed scores (weighted):")
            across_collapsed = across_score.collapse(weighted=True)
            print(across_collapsed)
            
            # Process WITHIN task
            print("\nCreating within-speaker task")
            within_output_csv = f"{accent.lower()}_dev_within_scores.csv"
            within_task = Task(
                dataset,
                on="#phone",
                by=["next-phone", "prev-phone", "speaker"]
            )
            
            print("Computing within-speaker scores with angular distance")
            within_score = Score(within_task, "angular")
            
            print(f"Writing within-speaker results to {within_output_csv}")
            within_score.write_csv(within_output_csv)
            
            print("Within-speaker collapsed scores (weighted):")
            within_collapsed = within_score.collapse(weighted=True)
            print(within_collapsed)
            
            print(f"Successfully processed {accent} (both across and within)")
            return True
            
        except Exception as e:
            print(f"Error processing {accent}: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def process_all_accents(self, accents: List[str]):
        """
        Process ABX tasks for all specified accents.
        
        Args:
            accents: List of accent names to process
        """
        success_count = 0
        failed_accents = []
        
        for accent in accents:
            success = self.process_accent(accent)
            if success:
                success_count += 1
            else:
                failed_accents.append(accent)
            print()  # Add blank line between accents
        
        # Print summary
        print("="*60)
        print("PROCESSING SUMMARY")
        print("="*60)
        print(f"Total accents: {len(accents)}")
        print(f"Successfully processed: {success_count}")
        print(f"Failed: {len(failed_accents)}")
        
        if failed_accents:
            print(f"Failed accents: {', '.join(failed_accents)}")
        
        print("All accents have been processed.")


def main():
    """Main function to run the ABX processor."""
    # List of all accents to process
    ACCENTS = [
        "American",
        "British", 
        "Indian",
        "Chinese",
        "Japanese",
        "Korean",
        "Russian",
        "Spanish",
        "Portuguese",
        "Canadian"
    ]
    
    # Configuration - these can be made command-line arguments if needed
    BASE_DIR = "your/path"
    FEATURES_DIR = "/features"
    TIMES_DIR = "/times"
    
    # Validate base directory
    if not os.path.exists(BASE_DIR):
        print(f"Error: Base directory does not exist: {BASE_DIR}")
        sys.exit(1)
    
    # Create and run processor
    processor = ABXProcessor(BASE_DIR, FEATURES_DIR, TIMES_DIR)
    processor.process_all_accents(ACCENTS)


if __name__ == "__main__":
    main()