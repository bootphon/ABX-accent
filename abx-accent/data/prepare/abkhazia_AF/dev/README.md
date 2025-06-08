
## Forced Alignment

Perform phone-level forced alignment on your own corpus of annotated audio files by following the steps provided in the [Abkhazia documentation](https://docs.cognitive-ml.fr/abkhazia/abkhazia_force_align.html).

### Directories and Files

* **`dev/`**:
  Contains forced alignment results for the development set. Each file is named as `dev_<accent>_align.align`, corresponding to a specific accent.

  * Example: `dev_american_align.align` contains forced alignment outputs for the American accent in the dev set.

* **`test/`**:
  Contains forced alignment results for the test set. Each file is named as `test_<accent>_align.align`, corresponding to a specific accent.

  * Example: `test_american_align.align` contains forced alignment outputs for the American accent in the test set.

