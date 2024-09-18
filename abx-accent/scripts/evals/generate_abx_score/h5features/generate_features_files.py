'''
Author: Manel KHENTOUT
Project: ABX-accent
Corpus: AESRC
2022
'''

#!/usr/bin/env python
import sys
import os
import abkhazia.utils as utils
from  abkhazia.kaldi.ark import scp_to_h5f


accents = ["American" , "British" , "Canadian" , "Chinese" , "Indian" , "Japanese" , "Korean" , "Spanish" , "Portuguese" , "Russian"]
accent_src = sys.argv[1]

def main():
    for  accent in accents:

        input_dir = accent_src+accent
        feats_file =input_dir+'/features/feats.scp'
        output_dir = input_dir+'/abx' 

        scp_to_h5f(feats_file, h5_file=input_dir+"/h5_file.h5f",h5_group='features',sample_frequency=100,tstart=0.0125,
        log=utils.logger.null_logger())
    
if __name__ == '__main__':
    sys.exit(main())
