# ABX Evaluation with FastABX

This workflow is based on [bootphon/fastabx](https://github.com/bootphon/fastabx).

# From `.h5f` Feature Files

1. **Convert features**
   Run the conversion script to transform `.h5f` feature files:v
   This script uses [`convert_features.py`](https://github.com/bootphon/fastabx/blob/main/scripts/convert_features.py).

2. **Run ABX evaluations**
   Execute:

   ```bash
   uv run run_fastabx.py
   ```

   



