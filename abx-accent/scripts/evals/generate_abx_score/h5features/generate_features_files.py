#!/usr/bin/env python
"""
Project: ABX-accent
Corpus: AESRC
2022
"""

import sys
import os
import abkhazia.utils as utils
from abkhazia.kaldi.ark import scp_to_h5f

# List of accents to process
ACCENTS = [
    "American", "British", "Canadian", "Chinese", 
    "Indian", "Japanese", "Korean", "Spanish", 
    "Portuguese", "Russian"
]

def main():
    """
    Convert feature files from Kaldi .scp format to HDF5 format
    for each accent in the AESRC corpus.
    
    Usage:
        python script.py <accent_source_directory>
    
    Where:
        <accent_source_directory> is the base directory containing 
        subdirectories for each accent
    """
    # Check if command line argument is provided
    if len(sys.argv) < 2:
        print("Error: Missing accent source directory")
        print("Usage: python script.py <accent_source_directory>")
        return 1
    
    accent_src = sys.argv[1]
    
    # Ensure accent_src ends with a trailing slash
    if not accent_src.endswith('/'):
        accent_src += '/'
        
    # Process each accent
    for accent in ACCENTS:
        input_dir = os.path.join(accent_src, accent)
        feats_file = os.path.join(input_dir, 'features', 'feats.scp')
        h5_file = os.path.join(input_dir, "h5_file.h5f")
        
        # Create output directory if it doesn't exist
        output_dir = os.path.join(input_dir, 'abx')
        os.makedirs(output_dir, exist_ok=True)
        
        print(f"Processing {accent} accent...")
        
        # Convert from SCP to H5F format
        try:
            scp_to_h5f(
                feats_file, 
                h5_file=h5_file,
                h5_group='features',
                sample_frequency=100,
                tstart=0.0125,
                log=utils.logger.null_logger()
            )
            print(f"Successfully converted {accent} features to HDF5 format")
        except Exception as e:
            print(f"Error processing {accent}: {str(e)}")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
