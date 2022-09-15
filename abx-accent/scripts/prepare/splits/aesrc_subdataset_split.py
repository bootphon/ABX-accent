'''
Project: ABX-accent
Corpus: AESRC
2022
'''
#input(Give speaker path,length) , out_put( file list with the input lenght (seconds))

#!/usr/bin/env python3
from pathlib import Path
import os
import sys
import ntpath
import pandas as pd
import librosa
import shutil

path = sys.argv[1] #the path of the speaker folder
length = sys.argv[2] #Data length

def one_spk_list(spk_path, length):
    curr_length = 0
    files = os.listdir(spk_path)
    out = []
   
    for file in files:
        if file[-4:] == '.wav':
            file_path = os.path.join(path, file)
            arr, sr = librosa.load(file_path)
            curr_length += len(arr)/sr
            #10 min of the data files are on /derived_data_10 sub folder
            folder_dst = path+'/derived_data_10/'
            
            out.append(file)
            if curr_length > float(length) :
                for item in out:
                    
                    wav_dst = os.path.join(path, item)
                    shutil.move(wav_dst,folder_dst)

                    txt_src = item.replace('.wav', '.txt')
                    txt_dst = os.path.join(path, txt_src) 
                    shutil.move(txt_dst,folder_dst) 
		    
                    meta_src = item.replace('.wav', '.metadata')
                    meta_dst = os.path.join(path, meta_src)
                    shutil.move(meta_dst,folder_dst)		      
                
	         
                return out
           
    raise ValueError('Not enough data in {}, only {} s, expected at least {} s'.format(path, curr_length, length))

if __name__ == "__main__":
    
    one_spk_list(path, length)
