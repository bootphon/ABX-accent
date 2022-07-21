'''
Project: input(Give speaker path,length) , out_put( file list with the input lenght (seconds))
Corpus: AESRC
Author:
'''
#!/usr/bin/env python3
from pathlib import Path
import os
import sys
import ntpath
import pandas as pd
import librosa
import shutil

path = sys.argv[1]
length = sys.argv[2]
def one_spk_list(spk_path, length):
    curr_length = 0
    files = os.listdir(spk_path)
    out = []
   
    for file in files:
        if file[-4:] == '.wav':
            file_path = os.path.join(path, file)
            arr, sr = librosa.load(file_path)
            curr_length += len(arr)/sr
            #print(str(curr_length))
            folder_dst = path+'/derived_data_10/'
            #print("src_file :",file_path)
            #print("\ndst_folder:",folder_dst)
            out.append(file)
            if curr_length > float(length) :
                for item in out:
                    print(item)#the name of file
                    wav_dst = os.path.join(path, item)
                    shutil.move(wav_dst,folder_dst)

	    	    #copy the txt file too
                    txt_src = item.replace('.wav', '.txt')
                    txt_dst = os.path.join(path, txt_src) 
                    shutil.move(txt_dst,folder_dst) 
		    #copy
		    #metadata
                    meta_src = item.replace('.wav', '.metadata')
                    meta_dst = os.path.join(path, meta_src)
                    shutil.move(meta_dst,folder_dst)		      
                
	        #print("\nfiles to treat:", out) 
                return out
           
    raise ValueError('Not enough data in {}, only {} s, expected at least {} s'.format(path, curr_length, length))

if __name__ == "__main__":
    
    one_spk_list(path, length)
