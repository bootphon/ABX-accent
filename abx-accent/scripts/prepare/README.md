## Data Preparation

### Environment Setup

* `.gitlab-ci.yml`: Configuration file used to set up the environment for running the preparation scripts.

---

### Data Split Scripts

**Location:** `Split data scripts/`

These scripts are used to split the AESRC dataset into the following subsets:

* Six female and six male speakers per accent
* Two hours of speech for ABX testing
* Two minutes of speech per speaker for adaptation

---

### Scripts and Files

* `aesrc_gender_split.py`

  * Generates the `aesrc_speakers_list.txt` file
  * Requires **Python 3.6+**

* `aesrc_speakers_list.txt`

  * Contains lists of male and female speakers per accent
  * **Example format:**
    `American_M = ['G00007', 'G00550', ..., 'G00XXX']`
  * These lists can be used to select subsets for dev, test, and train sets

* `aesrc_dataset_split.py`

  * Generates lists of filenames based on the required data duration
  * In this study:

    * **10 minutes per speaker** for dev/test sets
    * **2 minutes per speaker** for adaptation

---

### Abkhazia Format Preparation

**Location:** `Abkhazia/`

After splitting, these scripts format the data according to the Abkhazia standard requirements.

---

### Dependencies

* Requires the packages listed in `setup.py`
