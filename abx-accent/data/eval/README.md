

ABX Accent Evaluation
=====================
 
This toolkit supports accent-based ABX evaluation on the AESRC (Accented English Speech Recognition Challenge) dataset using fastABX.

What It Does
------------
 - Prepares evaluation lists for accent discrimination tasks.

 - Computes ABX error rates across and within speakers.


Getting Started
---------------
1. Download AESRC dataset (requires request via this [website](https://www.nexdata.ai/company/sponsored-datasets)).

2. Organize it into the expected directory structure:

4. Execute the scripts:
 scripts/evals/... to run fastABX and average resulting scores.
```
  fastABX
  generate_item_files
```
* you can get all the item and features files in [this github](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/data/eval) repository.


Evaluation Modes
----------------
Across-speaker vs Within-speaker discrimination.

Within-context vs Any-context context conditioning.

Requirements
------------
Linux/macOS (Ubuntu 16.04+, tested on Debian/CentOS).

fastABX and necessary Python dependencies installed.

 Results
 -------
Output includes:

.item files (phoneme timestamps and labels for evaluation).

.abx_score and .abx_score_average folders with ABX error metrics for dev/test.

References
----------
Shi et al. (ICASSP 2021): AESRC dataset and challenge.

Poli et al., fastabx: efficient ABX discriminability computation 
