**Data Splits**
===============

The first step was to split the AESRC data into three sets: *test, dev, and train*.

- **dev and test**: Consist of two hours of speech, from 12 speakers (six females and six males), used for ABX. Each speaker provides two minutes of speech for adaptation.

- **train**: Includes all the data from the other speakers. Speakers in the dev and test sets are disjoint from those in the training set.

- **abx.csv & adapt.csv**:

 - abx.csv: Contains all files used for ABX.

 - adapt.csv: Contains all files used for adaptation. These global files list the filenames and related information used in our study from the AESRC dataset.

- **File Information:**

- **filename**: Name of the audio file.

- **accent**: The accent associated with the filename, from the ten American accents in the AESRC dataset.

- **study**: Either ABX or adaptation.

- **set**: dev or test (used for ABX), train (used for adaptation).

- **speaker**: The speaker identifier.

- **gender**: Female or Male.

Example:
  
===============  ==========  ==========  ==========  ==========  ==========
    filename       accent       study       set        speaker    gender
---------------  ----------  ----------  ----------  ----------  ----------
G00473S1202.wav   American       adapt      dev         G00473    Female
===============  ==========  ==========  ==========  ==========  ==========


- **speakers folders** : A list of the male and female speakers used used to obtain the scores shown in this study.

- **filenames folder** : A List of filenames used for ABX and Adaptation in the dev and test sets.
