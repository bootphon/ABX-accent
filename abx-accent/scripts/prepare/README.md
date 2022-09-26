Data preparation
================

- `.gitlab-ci.yml`: to setup the environment, uses for the preparation scripts.
- [Split data scripts](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/prepare/data_splits) : scripts used to split the AESRC dataset, on six Female and six Male, with two hours of speech for ABX and 2 min for adaptation for each accent.

  - `aesrc_gender_split.py`: used to generate the `aesrc_speakers_list.txt`.
  - `aesrc_speakers_list.txt`: contains list of all the female and male speakers for each accent.
  Example: American_M = ['G00007', 'G00550'...], for list of Male speakers for American accent that can be used to select directly the sublist uses for dev, test ...
  - `aesrc_dataset_split.py`: scripts used to generate a list of filenames according to the data length (on this study, we used 10 min for dev/test sets for ABXpy and 2 min for adaptation).
Requires python>=3.6 instead.
- [Abkhazia](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/prepare/abkhazia) : after the split step, we prepare it to get the standard format of Abkhazia.
Requires on the [setup.py](https://github.com/bootphon/ABX-accent/edit/main/abx-accent/scripts/prepare/Setup.py).


