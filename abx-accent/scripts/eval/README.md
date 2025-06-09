

Data evaluation
===============
   
Organization
-------------

The main modules and submodules:
-Prepare: for data preparation
- [fastABX](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/eval/fastABX) 

- [generate_item_files](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts/eval/generate_item_files)



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
      - [fastABX](https://github.com/bootphon/fastabx)
       - convert_all_features.sh
       - run_fastabx.py
    
