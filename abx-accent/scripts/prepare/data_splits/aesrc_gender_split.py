#!/usr/bin/env python3
"""
Project: ABX-accent
Corpus: AESRC
2022

This script splits the AESRC dataset by gender (Male/Female) for each accent
and creates test, dev, and train splits.
"""
import os
import librosa
import sys

def is_male(path):
    """Check if a speaker is male based on metadata file"""
    with open(path, 'r') as file:
        content = file.read()
    words = content.split()
    return 'Male' in words

def split_by_gender(path):
    """Split speakers by gender for a given accent"""
    male = []
    female = []
    speakers = os.listdir(path)
    
    for spk in speakers:
        spk_path = os.path.join(path, spk)
        if os.path.isdir(spk_path):
            # Get the first metadata file
            metadata_files = [f for f in os.listdir(spk_path) if f.endswith('.metadata')]
            if metadata_files:
                metadata = metadata_files[0]
                group = metadata[:6]  # Extract group ID
                
                if is_male(os.path.join(path, spk, metadata)):
                    male.append(group)
                else:
                    female.append(group)
    
    return male, female

def calculate_speaker_length(path):
    """Calculate total audio length for a speaker"""
    files = os.listdir(path)
    total_length = 0
    
    for file in files:
        if file.endswith('.wav'):
            file_path = os.path.join(path, file)
            audio, sample_rate = librosa.load(file_path)
            total_length += len(audio) / sample_rate
    
    return total_length

def get_length_dict(base_path, speaker_list):
    """Create dictionary of speaker IDs to their total audio length"""
    result_dict = {}
    for speaker in speaker_list:
        speaker_path = os.path.join(base_path, speaker)
        result_dict[speaker] = calculate_speaker_length(speaker_path)
    return result_dict

def create_split_files(speaker_dict, output_path, name):
    """Create test, dev, and train split files"""
    # Sort speakers by length, prioritizing those with at least 7 minutes
    min_threshold = 60 * 7  # 7 minutes in seconds
    sorted_speakers = sorted(
        speaker_dict, 
        key=lambda x: speaker_dict[x] if speaker_dict[x] >= min_threshold else max(speaker_dict.values()) + speaker_dict[x]
    )
    
    # Create test split (first 6 speakers)
    with open(os.path.join(output_path, f"{name}_test"), 'w') as f:
        for speaker in sorted_speakers[:6]:
            f.write(f"{speaker}\n")
    
    # Create dev split (next 6 speakers)
    with open(os.path.join(output_path, f"{name}_dev"), 'w') as f:
        for speaker in sorted_speakers[6:12]:
            f.write(f"{speaker}\n")
    
    # Create train split (remaining speakers)
    with open(os.path.join(output_path, f"{name}_train"), 'w') as f:
        for speaker in sorted_speakers[12:]:
            f.write(f"{speaker}\n")

if __name__ == '__main__':
    # Check for command line arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_path> <output_path>")
        sys.exit(1)
    
    data_input_path = sys.argv[1]
    out_path = sys.argv[2]
    
    # Ensure output directory exists
    os.makedirs(out_path, exist_ok=True)
    
    # Process each accent
    accents = os.listdir(data_input_path)
    processed_accents = []
    
    # Initialize gender lists for each accent
    gender_lists = {}
    
    for accent in accents:
        if accent not in processed_accents:
            accent_path = os.path.join(data_input_path, accent)
            
            # Skip if not a directory
            if not os.path.isdir(accent_path):
                continue
                
            # Split by gender
            male_speakers, female_speakers = split_by_gender(accent_path)
            gender_lists[accent] = [male_speakers, female_speakers]
            
            # Calculate lengths and create splits for male speakers
            male_lengths = get_length_dict(accent_path, male_speakers)
            create_split_files(male_lengths, out_path, f"{accent.split()[0]}_M")
            
            # Calculate lengths and create splits for female speakers
            female_lengths = get_length_dict(accent_path, female_speakers)
            create_split_files(female_lengths, out_path, f"{accent.split()[0]}_F")
            
            processed_accents.append(accent)
