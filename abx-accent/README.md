ABX-accent 
=============
To get started the abx_accent project, you need two main steps: 

- Prepare the development AESRC data.
- Evaluation software setup.
 
Organisation
------------

The main modules and other submodules.
```
abx-accent/
├──  scripts
│   └── prepare/
│   │   └── abkhazia
│   │   └── data_splits/
│   │   │   └── aesrc_dataset_split.py
│   └── evals/
│   │   └── generate_item_files/
│   │   │   └── aesrc_item.py
│   │   └── generate_abx_score/
│   │   │   └── ABXpy/
│   │   │   │   └── ABXpy_env
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
, contains all the scripts you need on each step;

- Prepare scripts, the scripts used to prepare the dataset:
 
  - [Data split software](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/prepare/splits), after getting the AESRC dataset, we have to split it following three main steps:
  which is a dataset that contains ten different regional ac-
cents. From this dataset we make a split for each accent be-
tween a train, a dev and a test set, balancing for male and
female speakers (See Figure 1). The Test and dev sets con-
sist in two hours of speech for each accents, with six fema
  - sets split (test/dev/train); From this dataset of the ten accent has a training set, a dev and a test set, each containing different speakers.
  - speakers and gender split : balancing for male and female speakers with six Female and six Male for (test/dev) with 2hours of audio speech that will be used for ABX and to allow for speaker adaptation(adapt), the dev and test set provide for each speaker a 2min adaptation set.

  - [Abkhazia software](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/prepare/abkhazia).
  
- Evals softwares
 
  - [ABXpy software](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/eval/abx).
  - [Average score](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/eval/average).


**[Data](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/data)**

- Data prepare

  - [Data split](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/data/prepare/data_splits) First step is to split the data according to the number of the speakers you need, the gender and the duration of data for each speaker that will be used for the evaluation   and the adaptation.Scripts used in this [section](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/prepare/splits).

  - [Abkhazia](https://github.com/bootphon/abkhazia/tree/aesrc) uses the sets after the split step to obtain simple baselines for supervised ASR (using [Kaldi](http://kaldi-asr.org) ) and ABX tasks (using [ABXpy](https://github.com/bootphon/ABXpy) ). After validating the corpus to check that it is conform to Kaldi’s input format, we go to the next step:

  - [Forced Alignment](https://docs.cognitive-ml.fr/abkhazia/abkhazia_force_align.html), use the dataset after the preparation to do phone-level forced alignment.

- Data evals

  - [H5features](http://h5features.readthedocs.org/en/latest/h5features.html), Calculate the features, scripts used are in this [section](https://github.com/bootphon/AESRC/bin/evals/h5f).

  - `Item files`, generate the item files that will be used on ABXpy used are in this [section](https://github.com/bootphon/AESRC/bin/evals/items).

  - [The ABXpy Task module](https://docs.cognitive-ml.fr/ABXpy/ABXpy.html#task-module), is used for creating a new task and preprocessing, and calculate the distances necessary for task scores.

  - [Score average](https://github.com/bootphon/AESRC/results/average), Calculate the average of ABxpy task scores.


