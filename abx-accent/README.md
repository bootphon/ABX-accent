ABX-accent 
=============
To get started in the abx_accent project, you need two main steps: 

- Prepare the development AESRC dataset.

- Evaluation software setup.
 
Organization
------------

The main modules and other submodules.
```
abx-accent/
├──  scripts
│   └── prepare/
│   │   └── abkhazia
│   │   └── data_splits/
│   │   │   └── aesrc_gender_split.py
│   │   │   └── aesrc_dataset_split.py
│   │   │   └── aesrc_speakers_list.txt
│   └── evals/
│   │   └── generate_item_files/
│   │   │   └── aesrc_item.py
│   │   └── generate_abx_score/
│   │   │   └── ABXpy/ABXpy
│   │   │   └── across_task.sh
│   │   │   └── within_task.sh
│   │   │   └── abx_score.sh
│   │   │   └── abx_distance.sh
│   │   │   └── abx_analyze.sh
│   │   │   └── h5features/
│   │   │   │   └── generate_features_files.py
│   │   └── README.rst
│   │   └── average_abx_score/
│   │   │   │   └── average_abx_score.py
│   └── README.rst
├── data
│   └── prepare/
│   │   └── data_splits/
│   │   │   └── abx_files.csv
│   │   │   └── adapt_files.csv
│   │   └── abkhazia
│   │   │   └── forced_alignment
│   └── evals/
│   │   └── item_files/
│   │   │   └── dev_set
│   │   │   └── test_set
│   │   └── abx_score/
│   │   │   └── across_task
│   │   │   └── within_task
│   │   └── abx_score_average/
│   │   │   └── dev_set
│   │   │   └── test_set
│   └── README.rst
│README.rst
```

**[Scripts](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts)**
: contains all the scripts you need for each step.

- [Prepare scripts](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/prepare), scripts used to prepare the dataset:
 
  - [``Data split scripts``](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/prepare/splits), after getting the AESRC dataset, we have to split it following three main steps:
   - ``sets split`` (test/dev/train): split this dataset of the ten accent has on training set, a dev and a test set, each containing different speakers.
   - ``speakers and gender split``: balancing for male and female speakers, with six Female and six Male for (test/dev) and the rest for train set.
   - ``speech duration``: 10 min for each speaker on (test and dev) sets, which is 2 hours of audio speech on total and that will be used for ABX. The dev and test set provide for each speaker a 2 min adaptation set. The rest of the data used for train.
   
     ![](pictures/aesrc2.png)
     
  - [``Abkhazia's software``](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/prepare/abkhazia): provides a standard format for the dataset, used for ABXpy.
  
- [``Evals scripts``](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/evals), scripts used for the evaluation process:
 
  - [``ABXpy package``](https://github.com/bootphon/ABXpy), is used  for computing the scores of two tasks (across and within tasks) for (test/dev) sets.
  - [``ABX score average``](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/eval/average), is used to calculate the average of the ABX score for each task (across/within). This is using to compare between the dev/test average for each task and the other process used for training set.


**[Data](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/data)**, on this repository, we have also two main modules:

- [``Data prepare``](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/data/prepare)

  - [``Data split``](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/data/prepare/data_splits), to resume all the splits, you have two general files (`abx_files.csv` and `adapt_files.csv`), for each one you have the list of the filename, with it's own information   (accent: one of the ten accents, study:abx or adapt, speaker: which speaker, gender:Male or Female), you can use to rebuild the sets used to get the results on this repository.
  

  - [``Abkhazia``](https://github.com/bootphon/abkhazia/tree/aesrc) uses the sets after the split step to obtain the standard format for the dataset and then validate the corpus to check that it is conformed to Kaldi’s input format.

  - [``Forced Alignment``](https://docs.cognitive-ml.fr/abkhazia/abkhazia_force_align.html), use the dataset after the preparation to do phone-level forced alignment. If everything went right, you should be able to find your alignment in `corpus/align/alignments.txt`.

- [``Data evals``](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/data/evals), after preparation of the dataset on (test/dev) sets, we used ABX to evaluate the prepared dataset.

  - [``The ABXpy task``](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/data/evals/abx_score), contains two subfolders (across_task /within_task) each contains the abx task result.

  - [``Abx score average``](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/data/evals/average_abx_score), the average of ABX task scores for each accent.


