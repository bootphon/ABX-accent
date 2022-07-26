#!/usr/bin/env python

#AESRC dataset: split each accent on M/F for test,dev and train

import os
import librosa

def isMale(path):
    with open(path, 'r') as file:
        s = file.read()
    l = s.split()
    if 'Male' in l :
        return 1
    else:
            return 0


def split(path):
    male = []
    female = []
    speakers = os.listdir(path)
    for spk in speakers:
        if os.path.isdir(os.path.join(path, spk)):
            metadata = os.listdir(os.path.join(path, spk))[0]
            grp = metadata[:6]
            if isMale(os.path.join(path, spk, metadata)) :
                male.append(grp)
            else:
                female.append(grp)
    return male, female
        
def length_list(path, list):
    res_dict = {}
    for spk in list:
        spk_path = os.path.join(path, spk)
        res_dict[spk] = spk_length(spk_path)
    return res_dict

def spk_length(path):
    files = os.listdir(path)
    length = 0
    for file in files :
        if file[-4:] == '.wav' :
            file_path = os.path.join(path, file)
            arr, sr = librosa.load(file_path)
            length += len(arr)/sr
    return length
    
def output_txt(D, outpath, name):
    keys = sorted(D, key=lambda x: D[x] if D[x] >= 60*7 else max(D.values()) + D[x])
    
    with open(os.path.join(outpath, name + '_test'), 'w') as f:
        for key in keys[:6]:
            f.write(key)
            f.write('\n')
            
    with open(os.path.join(outpath, name + '_dev'), 'w') as f:
        for key in keys[6:12]:
            f.write(key)
            f.write('\n')
    
    with open(os.path.join(outpath, name + '_train'), 'w') as f:
        for key in keys[12:]:
            f.write(key)
            f.write('\n')
    
if __name__ == '__main__':
    #data_input_path   
    accents = os.listdir(data_input_path)
        
    gender_index = {'American English Speech Data': [American_M, American_F], 'Canadian English Speech Data': [Canadian_M, Canadian_F], 'Indian English Speech Data': [Indian_M, Indian_F], 'Korean Speaking English Speech Data': [Korean_M, Korean_F], 'Russian Speaking English Speech Data': [Russian_M, Russian_F], 'British English Speech Data': [British_M, British_F], 'Chinese Speaking English Speech Data': [Chinese_M, Chinese_F],'Japanese Speaking English Speech Data':  [Japenese_M, Japenese_F], 'Portuguese Speaking English Speech Data': [Portugese_M, Portugese_F], 'Spanish Speaking English Speech Data': [Spanish_M, Spanish_F]}
    
    Done = []
    
    for accent in accents:
        if accent not in Done:
            data_path = os.path.join(data_input_path, accent)
            D = length_list(data_path, gender_index[accent][0])
            output_txt(D, out_path, accent.split()[0] + '_M')
            D = length_list(data_path, gender_index[accent][1])
            output_txt(D, out_path, accent.split()[0] + '_F')
        
    
    
    #print(spk_length(os.path.join(american_path, American_M[0])))
    
    
    

