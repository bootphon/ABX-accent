Data preparation
================
 
- `Split data scripts <https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/prepare/splits>`_ : scripts used to splits the AESRC dataset, on six Female and six Male with two hours of speech for ABX and 2min for adatptation for each accent.

  - `aesrc_gender_split.py`: used to generate the `aesrc_speakers_list.txt`.
  - `aesrc_speakers_list.txt`: contains list of all the female and male speakers for each accents.Example: `American_M = ['G00007', 'G00550'...]`, for list of Male speakers for American accent that can be used to select directly the sublist uses for dev, test ...
  - `aesrc_dataset_split.py`: scripts used to generate a list of filenames according to the data length ( on this study we used 10 min for dev/test sets for ABXpy and 2min for adaptation).
  
- `Abkhazia <https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/prepare/abkhazia>`_ : after the split step, we prepare it to get the standard format of Abkhazia.


