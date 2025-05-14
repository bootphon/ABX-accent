


# ABX Evaluation with FastABX

This workflow is based on [bootphon/fastabx](https://github.com/bootphon/fastabx).

## From `.h5f` Feature Files

1. **Convert features**
   Run the conversion script to transform `.h5f` feature files:

   ```bash
   bash convert_all*_features.sh
   ```

   This script uses [`convert_features.py`](https://github.com/bootphon/fastabx/blob/main/scripts/convert_features.py).

2. **Run ABX evaluations**
   Execute:

   ```bash
   python run_fastabx_across_all*.py
   ```

   This script is based on `run_fastabx-across.py`.

**Note:** `all*` refers to the 10 different accents being processed.


