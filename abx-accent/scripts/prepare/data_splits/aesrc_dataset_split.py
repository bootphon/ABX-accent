#!/usr/bin/env python3
"""
Project: ABX-accent
Corpus: AESRC
2022

This script selects audio files for a speaker up to a specified duration length
and moves them to a derived_data_10 folder.

Usage: python3 script.py <speaker_path> <duration_in_seconds>
"""
import os
import sys
import shutil
import librosa
from pathlib import Path

def one_spk_list(spk_path, length):
    """
    Process one speaker's files and move them to the derived data folder
    when the accumulated duration exceeds the specified length.
    
    Args:
        spk_path (str): Path to the speaker's folder
        length (str): Target duration in seconds
        
    Returns:
        list: List of processed files
        
    Raises:
        ValueError: If there's not enough data to reach the target length
    """
    curr_length = 0
    files = os.listdir(spk_path)
    out = []
    
    # Create destination folder if it doesn't exist
    folder_dst = os.path.join(spk_path, 'derived_data_10')
    os.makedirs(folder_dst, exist_ok=True)
   
    for file in files:
        if file.endswith('.wav'):
            file_path = os.path.join(spk_path, file)
            arr, sr = librosa.load(file_path)
            curr_length += len(arr) / sr
            
            out.append(file)
            
            if curr_length > float(length):
                # Move all collected files to the destination folder
                for item in out:
                    # Move wav file
                    wav_src = os.path.join(spk_path, item)
                    shutil.move(wav_src, folder_dst)
                    
                    # Move associated txt file
                    txt_src = item.replace('.wav', '.txt')
                    txt_path = os.path.join(spk_path, txt_src)
                    if os.path.exists(txt_path):
                        shutil.move(txt_path, folder_dst)
                    
                    # Move associated metadata file
                    meta_src = item.replace('.wav', '.metadata')
                    meta_path = os.path.join(spk_path, meta_src)
                    if os.path.exists(meta_path):
                        shutil.move(meta_path, folder_dst)
                
                return out
           
    raise ValueError(f'Not enough data in {spk_path}, only {curr_length:.2f}s, expected at least {length}s')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <speaker_path> <duration_in_seconds>")
        sys.exit(1)
        
    path = sys.argv[1]  # Path to the speaker folder
    length = sys.argv[2]  # Target data length in seconds
    
    one_spk_list(path, length)
