**Data Splits**
===============
The first step done was, the AESRC data splits on three sets: **test**, *dev* and *train* sets, we focuson dev and test sets, which  consist of two hours of speech, within 12 speakers, including six Females and six Males using for ABX, and 
two minutes from each speaker for adaptation. 

All the data from the other speakers is included into the train set. Speakers from the dev and test sets are disjoints from those of the training set. 
To resplit the raw data, `here <https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/prepare/splits>`_ are the scripts used .

- Two global csv files(*abx.csv* & *adapt.csv* ):
the list of the filenames we used on our study from the AESRC dataset:

    - *abx.csv* for files used for ABXpy.
    - *adapt.csv* for files used for adaptation.
Both global csv files contain for each audio file the following informations:
    - *filename*: name of the audio filename.
    - *accent*: which accent bellow the filename from the ten American accents of AESRC dataset
    *the ten accents are : American,British,Canadian,Chinese,Indian,Japanese,Korean,Portuguese,Spanish,Russian.

    - *study*: ABX or adaptation
    - *set* : dev or test
    - *speaker* : which speaker.
    - *gender* : Female or Male
    
Example:
  
===============  ==========  ==========  ==========  ==========  ==========
    filename       accent       study       set        speaker    gender
---------------  ----------  ----------  ----------  ----------  ----------
G00473S1202.wav   American       adapt      dev         G00473    Female
===============  ==========  ==========  ==========  ==========  ==========


You can get the list of the filename from the csv file according to the accent,study,... you need on your study.


- **Speakers folder**:
the list of the Male and Female speakers we used to get the scores shows in this study 

- **filenames folder**:
List of filenames used for ABX and Adaptation for dev and test set.
