#!/usr/bin/env python
"""
Project: ABX-accent
Corpus: AESRC
2022

This script generates an ABX item file from the AESRC corpus alignments.
"""

import argparse
import os
import sys
import abkhazia.corpus.prepare.aesrc_preparator as aesrc
import abkhazia.utils as utils
from abkhazia.utils.abkhazia2abx import alignment2item
from abkhazia.corpus import Corpus

def main():
    """Generate an ABX item file from the AESRC corpus alignments."""
    # Define and parse input arguments
    parser = argparse.ArgumentParser(
        description='Generate an ABX item file from the AESRC corpus')
    
    parser.add_argument(
        'alignment_file', 
        help='Path to the alignment file'
    )
    
    parser.add_argument(
        'corpus_dir',
        help='Path to the AESRC corpus directory'
    )
    
    parser.add_argument(
        'item_file',
        help='Path where the item file will be written'
    )
    
    parser.add_argument(
        '-b', '--aesrc-dir', 
        help='Path to the raw AESRC corpus to prepare',
        default=None
    )
    
    args = parser.parse_args()
    
    # If aesrc_dir is not specified, use corpus_dir
    if args.aesrc_dir is None:
        args.aesrc_dir = args.corpus_dir
    
    # Setup the log
    log = utils.logger.get_log(verbose=False, header_in_stdout=False)
    
    # Load AESRC in abkhazia format
    try:
        log.info(f'Loading corpus from {args.corpus_dir}...')
        corpus = Corpus.load(args.corpus_dir)
    except Exception as e:
        log.error(f"Failed to load corpus: {e}")
        return 1
    
    # Generate the item file
    try:
        log.info(f'Generating the item file at {args.item_file}...')
        alignment2item(
            corpus, 
            args.alignment_file, 
            args.item_file, 
            segment_extension='single_phone',
            exclude_phones=[], 
            njobs=4, 
            verbose=1,
            ali_with_phone_proba=False
        )
        log.info('Item file generation completed successfully.')
    except Exception as e:
        log.error(f"Failed to generate item file: {e}")
        return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
