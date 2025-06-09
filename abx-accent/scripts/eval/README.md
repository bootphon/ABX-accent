

Data evaluation
===============
   
Organization
-------------

The main modules and submodules:
-Prepare: for data preparation
- [fastABX](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/eval/fastABX) : 

- [H5features](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/eval/generate_abx_score/h5features): the features can be calculated in numpy via external tools, and made compatible with this package with the `h5features module`. - `generate_features_files.py`, generate the `h5_file.h5f`file on each input dataset.        




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
     - Prepare scripts:
       - data_splits:
         aesrc_dataset_split.py
         aesrc_gender_split.py
      
    - eval scripts:
       - item files: 
          run `python3 aesrc_item.py input output`
          input:alignment_file corpus_dir
          output:item_file
          
       - features files:
           run `python3 generate_features_files.py input output`
           input:feats.scp
           output:h5_file.h5f

      - fastABX
      convert_all_features.sh
      run_fastabx.py
    
