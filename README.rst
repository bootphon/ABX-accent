.. image:: https://anaconda.org/coml/abx/badges/version.svg
    :target: https://anaconda.org/coml/abx


AESRC dataset
==============
The Accented English Speech Recognition Challenge is a
dataset that contains ten different regional accents.

Organisation
------------

The main modules and other submodules.

- `Abkhazia 
  <https://github.com/bootphon/abkhazia/tree/aesrc>`_
  makes it easy to obtain simple baselines for
  supervised ASR (using `Kaldi<http://kaldi-asr.org>` and ABX tasks
  (using ABXpy<https://github.com/bootphon/ABXpy>.

- `Splits data`
  test and dev sets consist in two hours of speech within 12 speakers
  including six Females and six Males. All the data from the
  other speakers is included into the train set.

- `Forced Alignment
  <https://docs.cognitive-ml.fr/abkhazia/abkhazia_force_align.html>`_
  

- `H5features
  <http://h5features.readthedocs.org/en/latest/h5features.html>`_ 
  The features can be calculated in numpy via external tools, and made compatible with this package with the `h5features module`.

- `Item files` 
  generate the item files that will be used on ABX.
  
 ###ABX

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

  



