
Data evaluation
===============
- [H5features](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/evals/generate_abx_score/h5features): the features can be calculated in numpy via external tools, and made compatible with this package with the `h5features module`.

      - `generate_features_files.py`, generate the `h5_file.h5f`file on each input dataset.
    
- [Item files](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/evals/generate_item_files) : generate the item files that will be used on ABX.
    - 
- [Task module](https://docs.cognitive-ml.fr/ABXpy/ABXpy.html#task-module), is
    used for creating a new task and preprocessing.
- [Distances package](https://docs.cognitive-ml.fr/ABXpy/ABXpy.distances.html>`_ is
    used for calculating the distances necessary for the score
    calculation.

- [Score module](https://docs.cognitive-ml.fr/ABXpy/ABXpy.html#score-module)
    is used for computing the score of a task.

- [Analyze module](https://docs.cognitive-ml.fr/ABXpy/ABXpy.html#analyze-module)
    is used for analysing the results.
    
- [Score average](https://github.com/bootphon/AESRC/results/average),to generate the score average. 
    

