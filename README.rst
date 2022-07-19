.. image:: https://anaconda.org/coml/abx/badges/version.svg
    :target: https://anaconda.org/coml/abx

AESRC dataset
==============
The Accented English Speech Recognition Challenge is a
dataset that contains ten different regional accents.

Organisation
------------

The main modules and other submodules.
- `Àbkhazia 
<https://docs.cognitive-ml.fr/abkhazia>`_ is used for creating the format of the data.

- `Splits data`
test and dev sets consist in two hours of speech within 12 speakers
including six Females and six Males. All the data from the
other speakers is included into the train set.

- `Forced Alignment
<https://docs.cognitive-ml.fr/abkhazia/abkhazia_force_align.html>ìs used for 

- `H5features
<http://h5features.readthedocs.org/en/latest/h5features.html>` _ The features can be calculated in numpy via external tools, and made compatible with this package with the `h5features module

- `Item files

- `task module
  <https://docs.cognitive-ml.fr/ABXpy/ABXpy.html#task-module>`_ is
  used for creating a new task and preprocessing.

- `distances package
  <https://docs.cognitive-ml.fr/ABXpy/ABXpy.distances.html>`_ is
  used for calculating the distances necessary for the score
  calculation.

- `score module
  <https://docs.cognitive-ml.fr/ABXpy/ABXpy.html#score-module>`_
  is used for computing the score of a task.

- `analyze module
  <https://docs.cognitive-ml.fr/ABXpy/ABXpy.html#analyze-module>`_
  is used for analysing the results
  
