# How to Split the Data

## Preparation
1. Prepare the AESRC dataset
2. Copy the dataset to the work folder

## Gender Split Process
1. Run the script to split the dataset by gender:
   ```
   python3 aesrc_gender_split.py <dataset_path>
   ```
   - **Input**: Dataset path
   - **Output**: An output file containing Male and Female sublists for each accent

You can see the [aesrc_speakers_list.txt]() for the lists we obtained after the split.

## Data Split Process
1. Create two folders:
   - `derived_data_10`: Contains files with 10 minutes per speaker (total duration of 2 hours)
   - `derived_data_2`: Contains files with 2 minutes per speaker

2. Run the dataset splitting script:
   ```
   python3 aesrc_dataset_split.py <dataset_path> <duration>
   ```
   - **Input**: 
     - Dataset path
     - Duration (in seconds): 600 for 10 min/speaker or 120 for 2 min/speaker
   - **Output**: Audio files with specified duration per speaker

3. First, split the dataset to get 10 minutes for each speaker (total 2 hours: 1 hour for male speakers and 1 hour for female speakers) for test and dev sets

4. Then, from the remaining files, run the script again to get files with 2 minutes per speaker
