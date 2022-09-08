**Data Splits**
===============
split the AESRC data on; *test* and *dev* sets consist in two hours of speech
within 12 speakers, including six Females and six Males using for ABX and 
2minutes from each speaker for adaptation. 
All the data from the other speakers is included into the train set. Speakers from the dev and test sets are disjoints from those of the training set. Scripts used on this section.

Two global csv files(*abx.csv* & *adapt.csv* ):
the list if the filenames we used on our study from the AESRC dataset:

    - *abx.csv* for files used for ABXpy.
    - *adapt.csv* for files used for adaptation.
Both global csv files contain for each audio file the following informations:
    - *filename*: name of the audio filename.
    - *accent*: which accent bellow the filename from the ten American accents of AESRC dataser
    *the ten accents are : American,British,Canadian,Chinese,Indian,Japanese,Korean,Portuguese,Spanish,Russian.

    - *study*: ABX or adaptation
    -*set* : dev or test
    -*speaker* : which speaker.
    -*gender* : Female or Male
Example:
   filename        accent    study   set   speaker  gender
G00473S1202.wav   American   adapt   dev   G00473   Female
You can get the list of the filename from the csv file according to the accent,... you need on your study.


**Speakers**:
the list of the Male and Female speakers we used to get the scores shows in this study 

**filenames**:
List of filenames used for ABX and Adaptation for dev and test set.