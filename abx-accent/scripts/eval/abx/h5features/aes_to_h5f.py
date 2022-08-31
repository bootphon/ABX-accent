'''
Project: ABX-accent
Corpus: AESRC
2022
'''
#!/usr/bin/env python
#

import sys
import os
import abkhazia.utils as utils
from  abkhazia.kaldi.ark import scp_to_h5f

##### AESRC Corpus #####
#         American      #
#         British       #
#         Canadian      #
#         Chinese       #
#         Indian        #
#         Japanese      #
#         Korean        #
#         Spanish       #
#       Portuguese      #
#          Russian      #
#########################

accents = ["American" , "British" , "Canadian" , "Chinese" , "Indian" , "Japanese" , "Korean" , "Spanish" , "Portuguese" , "Russian"]

def main():
    for  accent in accents:

        input_dir = "/scratch2/mkhentout/AESRC_2H/results/test/"+accent
        feats_file =input_dir+'/features/feats.scp'

        #output dir : '/scratch2/mkhentout/AESRC_2H/results/test/$Accent'/abx
        output_dir = input_dir+'/abx' 

        print("\nthe input path = ",input_dir)
        print("feats_file = ",feats_file)
        print("output_dir = ",output_dir)
        
        scp_to_h5f(feats_file, h5_file=input_dir+"/h5_file.h5f",h5_group='features',sample_frequency=100,tstart=0.0125,
        log=utils.logger.null_logger())
    
if __name__ == '__main__':
    sys.exit(main())