Data
=======

**Data preparation**

- ``Data splits`` :
The `data_splits/` folder contains the results of splitting the raw AESRC dataset into training, development, and test sets.
- ``Abkhazia`` : 
This step processes the split data into a standard format compatible with ABXpy. Follow the instructions in the `abkhazia/` folder to generate the formatted corpus.
- ``Forced alignment`` : 
Phone-level alignments are generated using the Abkhazia toolkit. The output files are located in the `forced_alignment/` directory.

**Data evaluation**

- ``Item files`` : 
ll item files required for ABX evaluations are available in the `item_files/` folder, organized by dataset `(dev_set and test_set)`.
- ``ABX scores`` : 
After running the evaluation using the prepared data and forced alignment outputs, ABXpy scores are saved in the `abx_score/` folder.
- ``Average score`` : 
Final ABX average scores per task and accent are stored in the `abx_score_average/` folder.
