
Data evaluation
===============
   
Organisation
-------------

The main modules and submodules.
- [Item files](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/evals/generate_item_files) : generate the item files that will be used on ABX.
    - `aesrc_item.py` : scripts used to generate an ABX item file from the AESRC corpus.

- [H5features](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/evals/generate_abx_score/h5features): the features can be calculated in numpy via external tools, and made compatible with this package with the `h5features module`.
    - `generate_features_files.py`, generate the `h5_file.h5f`file on each input dataset.        
- [Task module](https://docs.cognitive-ml.fr/ABXpy/ABXpy.html#task-module) : is used for creating a new task and preprocessing.
    - [across task](https://github.com/bootphon/ABX-accent/blob/main/abx-accent/scripts/evals/generate_abx_score/across_task.sh) :`within_task.sh` to generate the across task file using the item file.
    - [within task](https://github.com/bootphon/ABX-accent/blob/main/abx-accent/scripts/evals/generate_abx_score/within_task.sh) : `within_task.sh` to generate the within task file using the item file.
- [ABX distances](https://docs.cognitive-ml.fr/ABXpy/ABXpy.distances.html) : the script `abx_distance.sh` used for calculating the distances necessary for the score calculation.
- [Score module](https://docs.cognitive-ml.fr/ABXpy/ABXpy.html#score-module) : the `abx_score.sh` script  used for computing the score of a task.
- [Analyze module](https://docs.cognitive-ml.fr/ABXpy/ABXpy.html#analyze-module) : the `abx_analyze.sh`script used for analyzing the results.
- [Score average](https://github.com/bootphon/AESRC/results/average) : the `abx_score_average.py` script to generate the abx score average. 
    
Pipeline example:
-----------------

 
| In                                          | Module   | Out             |
|---------------------------------------------|:--------:|----------------:|
|  data.item & parameters                     | task     |  data.abx      |
|  data.abx & data.features & distance        | distance |  data.distance |
|  data.abx &  data.distance                  | score    |  data.score    |
|  data.abx & data.score                      | analyse  |  data.csv      |



Installation
------------

The recommended installation on Linux and macOS is using [conda](https://docs.conda.io/en/latest/miniconda.html).

  `conda install -c coml abx`

Alternatively, you may want to install it from sources. First clone
this repository and go to its root directory. Then :

     conda env create -n abx -f environment.yml
     source activate abx
     make install
     make test

     - item files: 
      run `python3 aesrc_item.py input output`
      input:alignment_file corpus_dir
      output:item_file
      
     - features files:
     run `python3 generate_features_files.py input output`
     input:feats.scp
     output:h5_file.h5f
     
     - ABX tasks
     run `./across_task.sh input output`, `./within_task.sh input output`
     input:item_file, task_spec*
     output:(abx_task*)abx_across.abx, abx_within.abx
     
     - ABX distance
     run `./abx_score.sh input output`
     input: h5_file.h5f, abx_task, --normalization 1
     output: distance.distance
     
     - ABX score
     run `./abx_distance.sh input output`
     input: abx_task, distance.distance
     output: score.score
     
     - ABX analyze
     run `./abx_analyze.sh input output`
     input: score.score, abx_task
     output: task.csv
     
     - ABX score average
     run `python3 average_abx_score.py input output`
     input:task_within task_across 
     output:within_average_score across_average_score
     

     abx_task* : abx_across and abx_within
     across task_spec*: -o phone -a speaker -b prev-phone next-phone
     within task_spec*: -o phone -b speaker prev-phone next-phone
    
