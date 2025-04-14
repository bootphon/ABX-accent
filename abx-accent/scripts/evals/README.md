
Data evaluation
===============
   
Organization
-------------

The main modules and submodules:
- [ABXpy](https://github.com/bootphon/ABXpy) : for the ABX evaluation environment.
  
- [Item files](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/evals/generate_item_files) : generate the item files used by ABX.
    - `aesrc_item.py` : script used to generate ABX item files from the AESRC corpus.
- [H5features](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/evals/generate_abx_score/h5features): features can be computed using external tools and converted for use with this package via the `h5features module`.
    - `generate_features_files.py`, generates `h5_file.h5f`from each input dataset.
    -    
- [Task module](https://docs.cognitive-ml.fr/ABXpy/ABXpy.html#task-module) : used for creating new tasks and preprocessing.
    - [across task](https://github.com/bootphon/ABX-accent/blob/main/abx-accent/scripts/evals/generate_abx_score/across_task.sh) :generates the across-task file from an item file.
    - [within task](https://github.com/bootphon/ABX-accent/blob/main/abx-accent/scripts/evals/generate_abx_score/within_task.sh) : generates the within-task file from an item file.
      
- [ABX distances](https://docs.cognitive-ml.fr/ABXpy/ABXpy.distances.html) :   `abx_distance.sh` script computes distances required for score calculation.
- [Score module](https://docs.cognitive-ml.fr/ABXpy/ABXpy.html#score-module) : the `abx_score.sh` script computes task scores.
- [Analyze module](https://docs.cognitive-ml.fr/ABXpy/ABXpy.html#analyze-module) : the `abx_analyze.sh` script is used to analyze results.
- [Score average](https://github.com/bootphon/AESRC/results/average) : the `abx_score_average.py` script computes average ABX scores.
    
Pipeline example:
-----------------

 
| In                                          | Module   | Out             |
|---------------------------------------------|:--------:|----------------:|
|  data.item & parameters                     | Task     |  data.abx      |
|  data.abx & data.features & distance        | Distance |  data.distance |
|  data.abx &  data.distance                  | Score    |  data.score    |
|  data.abx & data.score                      | Analyse  |  data.csv      |



Installation
------------

The recommended installation for Linux/macOS is via [conda](https://docs.conda.io/en/latest/miniconda.html).

  `conda install -c coml abx`

Alternatively, to install from source:

     conda env create -n abx -f environment.yml
     source activate abx
     make install
     make test
     
Usage
=====
Generate Item files: 
`python3 aesrc_item.py input output`
      - input:alignment_file, corpus_dir
      - output:item_file
      
Generate Features files:
`python3 generate_features_files.py input output`
     - input:feats.scp
     - output:h5_file.h5f
     
Generate ABX tasks
`./across_task.sh input output` 
#or 
`./within_task.sh input output`
     - input:item_file, task_spec*
     - output:abx_task*
     
Compute ABX Distances
`./abx_score.sh input output`
     - input: h5_file.h5f, abx_task*, --normalization 1
     - output: distance.distance
     
Compute ABX Scores
`./abx_distance.sh input output`
     - input: abx_task*, distance.distance
     - output: score.score
     
Analyze ABX results
`./abx_analyze.sh input output`
     - input: score.score, abx_task*
     - output: task.csv*
     
Compute ABX score averages
`python3 average_abx_score.py input output`
     - input:task.csv* 
     - output:task_average_score.txt* 
     
Notation
========
- abx_task* : abx_across.abx or abx_within.abx.
- task_spec* :
  - Across task: -o phone -a speaker -b prev-phone next-phone
  - Within task: -o phone -b speaker prev-phone next-phone
- task.csv* :e.g within_task.csv or across_task.csv
- task_average_score.txt* :e.g within_average_score.txt or across_average_score.txt.
