
Evaluation software
=====================
To evaluate the AESRC dataset after the splitting setp, here are the steps to follow:

- `H5features <http://h5features.readthedocs.org/en/latest/h5features.html>`_ The features can be calculated in numpy via external tools, and made compatible with this package with the `h5features module`. Scripts used are on this `section <https://github.com/bootphon/AESRC/bin/evals/h5f>`_.    
    
- `Item files` generate the item files that will be used on ABX. Scripts used are on this `section <https://github.com/bootphon/AESRC/bin/evals/items>`_. 
    
- `Task module <https://docs.cognitive-ml.fr/ABXpy/ABXpy.html#task-module>`_ is used for creating a new task and preprocessing.
    
- `Distances package <https://docs.cognitive-ml.fr/ABXpy/ABXpy.distances.html>`_ is used for calculating the distances necessary for the score calculation.
    
- `Score module <https://docs.cognitive-ml.fr/ABXpy/ABXpy.html#score-module>`_ is used for computing the score of a task.
    
- `Analyze module <https://docs.cognitive-ml.fr/ABXpy/ABXpy.html#analyze-module>`_ is used for analysing the results. 
    
- `Score average <https://github.com/bootphon/AESRC/results/average>`_ , to generate the score average. 
    
