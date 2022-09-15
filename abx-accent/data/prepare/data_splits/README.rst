**Data Splits**
===============

The first step done was, the AESRC data splits on three sets: **test**, **dev** and **train** sets.
    - **dev** and **test** : consist of two hours of speech, within 12 speakers, including six Females and six Males using for ABX, and two minutes from each speaker for adaptation. 
    - **train** : include all the data from the other speakers. Speakers from the dev and test sets are disjoints from those of the training set.
    
To resplit the raw data, `here <https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/prepare/splits>`_ are the scripts used .

    - **abx.csv** & **adapt.csv**: abx.csv for files used for ABXpy et adapt.csv for files used for adaptation, this global files contain the list of the filenames and their informations that we used on our study from the AESRC dataset:

        - *filename*: name of the audio filename.
        - *accent*: which accent bellow the filename from the ten American accents of AESRC dataset.
        - *study*: ABX or adaptation.
        - *set* : dev or test.
        - *speaker* : which speaker.
        - *gender* : Female or Male.
        
Example:
  
===============  ==========  ==========  ==========  ==========  ==========
    filename       accent       study       set        speaker    gender
---------------  ----------  ----------  ----------  ----------  ----------
G00473S1202.wav   American       adapt      dev         G00473    Female
===============  ==========  ==========  ==========  ==========  ==========

- **Speakers folder** : List of the Male and Female speakers we used to get the scores shows in this study.

- **filenames folder** : List of filenames used for ABX and Adaptation for dev and test set.
