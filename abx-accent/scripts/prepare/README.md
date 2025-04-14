# Data Preparation

## Environment Setup
- `.gitlab-ci.yml`: Configuration file for setting up the environment used by the preparation scripts.

## Data Split Scripts
Location: [Split data scripts](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/prepare/data_splits)

These scripts are used to split the AESRC dataset into:
- Six female and six male speakers per accent
- Two hours of speech for ABX testing
- Two minutes of speech per speaker for adaptation 

### Scripts and Files
1. **`aesrc_gender_split.py`**: 
   - Generates the `aesrc_speakers_list.txt` file
   - Requires Python 3.6 or higher

2. **`aesrc_speakers_list.txt`**: 
   - Contains lists of all female and male speakers for each accent
   - Example format: `American_M = ['G00007', 'G00550', ..., 'G00XXX']`
   - These lists can be used to directly select subsets for dev, test, and train sets

3. **`aesrc_dataset_split.py`**: 
   - Generates lists of filenames according to the specified data length
   - In this study:
     - 10 minutes per speaker for dev/test sets (for ABXpy)
     - 2 minutes per speaker for adaptation

## Abkhazia Format Preparation
Location: [Abkhazia](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/prepare/abkhazia)

After splitting the data, these scripts prepare it in the standard format required by Abkhazia.

### Dependencies
- Requires packages specified in [setup.py](https://github.com/bootphon/ABX-accent/edit/main/abx-accent/scripts/prepare/Setup.py)
