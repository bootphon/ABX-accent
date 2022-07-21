.. image:: https://anaconda.org/coml/abx/badges/version.svg
    :target: https://anaconda.org/coml/abx


AESRC dataset
==============
The Accented English Speech Recognition Challenge is a
dataset that contains ten different regional accents.

Organisation
------------

The main modules and other submodules.

**Data prepare**

- `Abkhazia 
  <https://github.com/bootphon/abkhazia/tree/aesrc>`_
  makes it easy to obtain simple baselines for
  supervised ASR (using `Kaldi <http://kaldi-asr.org>`_) and ABX tasks
  (using `ABXpy <https://github.com/bootphon/ABXpy>`_).
   
  After validating the corpus to check that it is conform to Kaldi’s input format, we go to the splits step:
- `Splits data`
  test and dev sets consist in two hours of speech within 12 speakers
  including six Females and six Males using for ABx and 2minutes from each speaker for adapt.
  All the data from the other speakers is included into the train set.
  Speakers from the dev and test sets are disjoints from those of the training set.
  scripts used on this `section <https://github.com/bootphon/AESRC/splits>`_.
  And the `here<https://github.com/bootphon/AESRC/splits>`_ the list of speakers and filenames used.
  
   Once we split the dataset to test,dev and train, we 

- `Forced Alignment<https://docs.cognitive-ml.fr/abkhazia/abkhazia_force_align.html>`_, follow the steps in the link to do phone-level forced alignment on your own corpusof annotated audio files.
  
**Evals**

- `H5features
  <http://h5features.readthedocs.org/en/latest/h5features.html>`_ 
  The features can be calculated in numpy via external tools, and made compatible with this package with the `h5features module`.
  scripts used are on this _`section<https://github.com/bootphon/AESRC/evals/h5f>`_.
  
- `Item files` 
  generate the item files that will be used on ABX.scripts used are on this _`section _<https://github.com/bootphon/AESRC/evals/items>`_.
  


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
  is used for analysing the results.
  
- `score average<https://>`_ ,to generate the average of  
  
Licence
========

**Copyright 2022 CoML team (Inria, ENS, CNRS, EHESS)**

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

  



