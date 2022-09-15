ABX-accent 
==============
All you need to get started to work on the development data and evaluation of the Accented English Speech Recognition Challenge (AESRC) is:

- Prepare the development data.
- Evaluation software setup.
 
AESRC corpus contain ten accents: *American,British,Canadian,Chinese,Indian,Japanese,Korean,Portuguese,Spanish,Russian*
 
Organisation
------------

The main modules and other submodules.

**Data**

- Data prepare

  - `Data splits <https://github.com/bootphon/ABX-accent/tree/main/abx-accent/data/prepare/data_splits>`_
First step is to split the data according to the number of the speakers you need, the gender and the duration of data for each speaker that will be used for the evaluation   and the adaptation.
Scripts used in this `section <https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/prepare/splits>`_.

  - `Abkhazia <https://github.com/bootphon/abkhazia/tree/aesrc>`__
   uses the sets after the split step to obtain simple baselines for
   supervised ASR (using `Kaldi <http://kaldi-asr.org>`_) and ABX tasks
   (using `ABXpy <https://github.com/bootphon/ABXpy>`_).

 After validating the corpus to check that it is conform to Kaldi’s input format, we go to the next step:

  - `Forced Alignment <https://docs.cognitive-ml.fr/abkhazia/abkhazia_force_align.html>`_, use the dataset after the preparation to do phone-level forced alignment.

- Data evals

  - `H5features <http://h5features.readthedocs.org/en/latest/h5features.html>`_ 
   Calculate the features, scripts used are in this `section <https://github.com/bootphon/AESRC/bin/evals/h5f>`_.

  - `Item files` 
   generate the item files that will be used on ABXpy used are in this `section <https://github.com/bootphon/AESRC/bin/evals/items>`_.

  - `ABXpy Task module <https://docs.cognitive-ml.fr/ABXpy/ABXpy.html#task-module>`_ is
   used for creating a new task and preprocessing, and calculate the distances necessary for task scores.

  - `Score average <https://github.com/bootphon/AESRC/results/average>`_ Calculate the average of ABxpy task scores .

**Scripts**

- Prepare softwares
 
  - `Splits software <https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/prepare/splits>`_.
  - `Abkhazia software <https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/prepare/abkhazia>`_.
  
- Evals softwares
 
  - `ABXpy software <https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/eval/abx>`_.
  - `Average score <https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/eval/average>`_.


