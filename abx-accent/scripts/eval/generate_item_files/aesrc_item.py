#!/usr/bin/env python3
"""
Project: ABX-accent
Corpus: AESRC
2022

This script generates an ABX item file from the AESRC corpus using alignment data.
It converts alignment files into item files suitable for ABX discrimination tasks.
"""

import argparse
import os
import sys
import logging
from pathlib import Path

# Import abkhazia modules
try:
    import abkhazia.corpus.prepare.aesrc_preparator as aesrc
    import abkhazia.utils as utils
    from abkhazia.utils.abkhazia2abx import alignment2item
    from abkhazia.corpus import Corpus
except ImportError as e:
    print(f"Error: Failed to import abkhazia modules: {e}")
    print("Please ensure abkhazia is properly installed.")
    sys.exit(1)


class AESRCABXGenerator:
    """Generates ABX item files from AESRC corpus alignment data."""
    
    def __init__(self, corpus_dir: str, alignment_file: str, item_file: str, 
                 segment_extension: str = 'single_phone', exclude_phones: list = None,
                 njobs: int = 4, verbose: int = 1, ali_with_phone_proba: bool = False):
        """
        Initialize the ABX generator.
        
        Args:
            corpus_dir: Path to the AESRC corpus directory
            alignment_file: Path to the alignment file
            item_file: Path for the output item file
            segment_extension: Segmentation extension type
            exclude_phones: List of phones to exclude
            njobs: Number of parallel jobs
            verbose: Verbosity level
            ali_with_phone_proba: Whether to include phone probabilities
        """
        self.corpus_dir = Path(corpus_dir)
        self.alignment_file = Path(alignment_file)
        self.item_file = Path(item_file)
        self.segment_extension = segment_extension
        self.exclude_phones = exclude_phones or []
        self.njobs = njobs
        self.verbose = verbose
        self.ali_with_phone_proba = ali_with_phone_proba
        
        # Validate inputs
        self._validate_inputs()
        
        # Setup logging
        self.log = self._setup_logging()
    
    def _validate_inputs(self):
        """Validate input files and directories."""
        if not self.corpus_dir.exists():
            raise FileNotFoundError(f"Corpus directory does not exist: {self.corpus_dir}")
        
        if not self.alignment_file.exists():
            raise FileNotFoundError(f"Alignment file does not exist: {self.alignment_file}")
        
        # Ensure output directory exists
        self.item_file.parent.mkdir(parents=True, exist_ok=True)
    
    def _setup_logging(self) -> logging.Logger:
        """Setup logging for the script."""
        try:
            # Use abkhazia's logger if available
            return utils.logger.get_log(verbose=(self.verbose > 0), header_in_stdout=False)
        except Exception:
            # Fallback to standard logging
            logging.basicConfig(
                level=logging.INFO if self.verbose > 0 else logging.WARNING,
                format='%(asctime)s - %(levelname)s - %(message)s'
            )
            return logging.getLogger(__name__)
    
    def load_corpus(self) -> Corpus:
        """
        Load the AESRC corpus in abkhazia format.
        
        Returns:
            Loaded corpus object
        """
        self.log.info(f"Loading corpus from: {self.corpus_dir}")
        
        try:
            corpus = Corpus.load(str(self.corpus_dir))
            self.log.info(f"Successfully loaded corpus with {len(corpus.utts())} utterances")
            return corpus
        except Exception as e:
            self.log.error(f"Failed to load corpus: {e}")
            raise
    
    def generate_item_file(self, corpus: Corpus):
        """
        Generate the ABX item file from the corpus and alignment.
        
        Args:
            corpus: Loaded corpus object
        """
        self.log.info("Generating ABX item file...")
        self.log.info(f"Alignment file: {self.alignment_file}")
        self.log.info(f"Output item file: {self.item_file}")
        self.log.info(f"Segment extension: {self.segment_extension}")
        self.log.info(f"Excluded phones: {self.exclude_phones}")
        self.log.info(f"Number of jobs: {self.njobs}")
        
        try:
            alignment2item(
                corpus=corpus,
                alignment_file=str(self.alignment_file),
                item_file=str(self.item_file),
                segment_extension=self.segment_extension,
                exclude_phones=self.exclude_phones,
                njobs=self.njobs,
                verbose=self.verbose,
                ali_with_phone_proba=self.ali_with_phone_proba
            )
            self.log.info(f"Successfully generated item file: {self.item_file}")
        except Exception as e:
            self.log.error(f"Failed to generate item file: {e}")
            raise
    
    def run(self):
        """Run the complete ABX item generation process."""
        try:
            # Load the corpus
            corpus = self.load_corpus()
            
            # Generate the item file
            self.generate_item_file(corpus)
            
            self.log.info("ABX item generation completed successfully!")
            
        except Exception as e:
            self.log.error(f"ABX item generation failed: {e}")
            raise


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Generate an ABX item file from the AESRC corpus',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    # Required arguments
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
        help='Path for the output ABX item file'
    )
    
    # Optional arguments
    parser.add_argument(
        '-s', '--segment-extension',
        default='single_phone',
        help='Segmentation extension type'
    )
    parser.add_argument(
        '-e', '--exclude-phones',
        nargs='*',
        default=[],
        help='List of phones to exclude from the analysis'
    )
    parser.add_argument(
        '-j', '--njobs',
        type=int,
        default=4,
        help='Number of parallel jobs to use'
    )
    parser.add_argument(
        '-v', '--verbose',
        type=int,
        default=1,
        choices=[0, 1, 2],
        help='Verbosity level (0=quiet, 1=info, 2=debug)'
    )
    parser.add_argument(
        '--ali-with-phone-proba',
        action='store_true',
        help='Include phone probabilities in alignment'
    )
    parser.add_argument(
        '--validate-only',
        action='store_true',
        help='Only validate inputs without processing'
    )
    
    return parser.parse_args()


def main():
    """Main function."""
    args = parse_arguments()
    
    try:
        # Create the ABX generator
        generator = AESRCABXGenerator(
            corpus_dir=args.corpus_dir,
            alignment_file=args.alignment_file,
            item_file=args.item_file,
            segment_extension=args.segment_extension,
            exclude_phones=args.exclude_phones,
            njobs=args.njobs,
            verbose=args.verbose,
            ali_with_phone_proba=args.ali_with_phone_proba
        )
        
        if args.validate_only:
            print("✓ All inputs validated successfully!")
            print(f"Corpus directory: {args.corpus_dir}")
            print(f"Alignment file: {args.alignment_file}")
            print(f"Output item file: {args.item_file}")
        else:
            # Run the generation process
            generator.run()
        
        return 0
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())