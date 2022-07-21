#!/usr/bin/env python
#

import argparse
import os
import sys
import tempfile

import abkhazia.corpus.prepare.aesrc_preparator as aesrc
import abkhazia.utils as utils
from abkhazia.utils.abkhazia2abx import alignment2item
from abkhazia.corpus import Corpus

# The path to the raw Buckeye distribution
alignment_file = '/scratch2/mkhentout/AESRC_2H/results/dev/Spanish/align/alignment.txt'
corpus_dir = '/scratch2/mkhentout/AESRC_2H/results/dev/Spanish/data/'
item_file = '/scratch2/mkhentout/AESRC_2H/results/dev/Spanish/data/item_file.txt'

def main():
    # define and parse input arguments
    parser = argparse.ArgumentParser(
        description='Generate an ABX item file from the AESRC corpus')
    parser.add_argument(
        '-b', '--aesrc-dir', default=corpus_dir,help='path to the raw AESRC corpus to prepare'', default is %(default)s')
    
    args = parser.parse_args()

    # setup the log and tmpdir
     
 
    
    log = utils.logger.get_log(verbose=False, header_in_stdout=False)

    # load AESRC in abkhazia format
    corpus = Corpus.load(corpus_dir)
            
    log.info('generating the item file...')
    alignment2item(corpus, alignment_file, item_file, segment_extension='single_phone',
                   exclude_phones=[], njobs=4, verbose=1,
                   ali_with_phone_proba=False)
 

if __name__ == '__main__':
    sys.exit(main())
