# Item Files

Item files are required inputs for the ABXpy evaluation. These files define the minimal pair comparisons used to compute ABX scores.

Scripts for generating item files can be found in [this section](https://github.com/bootphon/AESRC/bin/evals/items).

## Contents

* **dev**: Contains item files for the development set, e.g., `dev_american_item.item`.
* **test**: Contains item files for the test set, e.g., `test_american_item.item`.

## Example Item File Format

| file        | onset  | offset | #phone | prev-phone | next-phone | speaker |
| ----------- | ------ | ------ | ------ | ---------- | ---------- | ------- |
| G00473S1001 | 0.5775 | 0.8775 | m      | aɪ         | ɪ          | G00473  |

Each row specifies a phone segment to be evaluated, along with its context and speaker identity.


