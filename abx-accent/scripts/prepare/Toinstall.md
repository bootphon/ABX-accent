# ABX-accent Installation Guide

## Prerequisites

### System Packages
```bash
# Install gawk
sudo apt-get install gawk
```

### SRILM Installation
SRILM cannot be installed automatically using the script alone. Follow these steps:

1. Download SRILM package from: http://www.speech.sri.com/projects/srilm/download.html
2. Rename the package to "srilm.tgz"
3. Copy the package to /tools
4. Run the installation script:
   ```bash
   /tools/extras/install_srilm.sh
   ```
5. Update your environment:
   ```bash
   source /tools/env.sh
   ```

## Python Dependencies

### Environment Setup
The project requires Python 3.8 and specific package versions.

### Fix Common Issues
If you encounter the "Couldn't find index page for matplotlib" error or other installation issues, first update your package management tools:

```bash
# Update pip and setuptools
sudo pip3 install -U pip setuptools

# Update Jinja2 (required for some dependencies)
sudo pip3 install -U jinja2
```

### Required Python Packages
Install the following packages in this order:

```bash
# Core dependencies
sudo pip3 install phonemizer
pip3 install matplotlib
sudo pip3 install progressbar2
sudo pip3 install argcomplete

# Specific version requirements
pip3 install h5py==2.10.0
```

## Troubleshooting

If you still encounter issues with matplotlib or other packages:
- Check your Python version with `python3 --version`
- Ensure pip is correctly linked to Python 3.8 with `pip3 --version`
- Try installing packages with the `--user` flag if you don't have admin rights
