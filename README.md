ABX-accent 
==============
The *ABX-accent* project is based on the preparation and evaluation of the Accented English Speech Recognition Challenge (AESRC) dataset [1], using ABXpy for evaluation [2][3]. This repository provides all the necessary tools and resources to carry out both dataset preparation and evaluation.

[The ABXpy](https://docs.cognitive-ml.fr/ABXpy/)  metric evaluate for a pair of sounds representations (A,B) from for example (”bap”,”bop”), the probability that the representation X of another instance of the sound ”bap” is closer to A than B. ABX error rate is computed by averaging over all the minimal pairs of phone trigram in the corpus. 
In this benchmark, we focus on the harder ABX across speaker metric, which uses X instances from a different speaker than the one of the pair(A,B).

[The Accented English Speech Recognition Challenge](https://arxiv.org/abs/2102.10233) consists of ten  different regional accents: American, British, Canadian, Chinese, Indian, Japanese, Korean, Portuguese, Spanish, Russian.

Start the project
-------------------
All you need to get started to work on the development data and the evaluation of AESRC is :

- [The scripts](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts) used for both the preparation and the evaluation process.
- [The result's data](https://github.com/bootphon/ABX-accent/tree/main/abx-accent/data) after the preparation and the evaluation process.

The setup procedure is described for Linux. It has been tested on several distributions (Ubuntu 16.04, Debian Jessie and CentOS 6). It should work as well on macOS.

Organization
------------

```
abx-accent/
├──  scripts
│   └── prepare/
│   │   └── data_splits
│   │   └── abkhazia
│   └── evals/
│   │   └── generate_item_files
│   │   └── generate_abx_score
│   │   └── abx_score_average
│   └── README.rst
├── data
│   └── prepare/
│   │   └── data_splits
│   │   └── abkhazia
│   │   │   └── forced_alignment
│   └── evals/
│   │   └── item_files
│   │   │   └── dev_set
│   │   │   └── test_set
│   │   └── abx_score
│   │   │   └── across_task
│   │   │   └── within_task
│   │   └── abx_score_average
│   │   │   └── dev_set
│   │   │   └── test_set
│   └── README.rst
│README.rst
```

License
--------

**Copyright 2022 CoML team (Inria, ENS, CNRS, EHESS)**

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

References 
-----------
- [1] Xian Shi, Fan Yu, Yizhou Lu, Yuhao Liang, Qiangze Feng, Daliang Wang, Yanmin Qian, and Lei Xie, “The accented english speech recognition challenge 2020: open datasets, tracks, baselines, results and methods,” in ICASSP 2021-2021 IEEE International Conference on Acoustics, Speech and Signal Processing       (ICASSP).IEEE, 2021, pp. 6918–6922.
  
- [2] Ewan Dunbar, Julien Karadayi, Mathieu Bernard, Xuan-Nga Cao, Robin Algayres, Lucas Ondel, Laurent Besacier, Sakriani Sakti, and Emmanuel Dupoux, “The zero resource speech challenge 2020: Discovering discrete subword and word units,” 2020.

- [3] Ewan Dunbar, Mathieu Bernard, Nicolas Hamilakis, Tu Anh Nguyen, Maureen de Seyssel, Patricia Roz ́e, Morgane Rivi`ere, Eugene Kharitonov, and Emmanuel Dupoux, “The zero resource speech challenge 2021: Spoken language modelling,” 2021.


