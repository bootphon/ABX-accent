ABX-accent 
==============
The ABX-accent, project based of the preparation and the evaluation of Accented English Speech Recognition Challenge (AESRC) data, using `ABXpy <https://docs.cognitive-ml.fr/ABXpy/>`_ for the evaluation,We provide in our github repository all the necessary elements for the preparation and evaluation process.

The ABXpy metric evaluate for a pair of sounds representations (A,B) from for example (”bap”,”bop”), the probability that the representation X of another instance of the sound ”bap” is closer to A than B. ABX error rate is computed by averaging over all the minimal pairs of phone trigram in the corpus. 
In this benchmark we focus on the harder ABX across speaker metric, which uses X instances from a different speaker than the one of the pair(A,B).

The `Accented English Speech Recognition Challenge (AESRC) <https://arxiv.org/abs/2102.10233>`_ consists of ten english accents: American, British, Canadian, Chinese, Indian, Japanese, Korean, Portuguese, Spanish, Russian.

Start the project
-------------------
All you need to get started to work on the development data and evaluation for AESRC is a:

- preparation and evaluation softwares.
- `The results data <https://github.com/bootphon/ABX-accent/tree/main/abx-accent/data>`_ after the preparation and the evaluation process.

The setup procedure is described for Linux. It has been tested on several distributions (Ubuntu 16.04, Debian Jessie and CentOS 6). It should work as well on MacOS.

Organisation
------------
abx-accent/
├── `data
<https://github.com/bootphon/ABX-accent/tree/main/abx-accent/data>`_ ( The preparation data and the data results after the evaluation. 
│   └──prepare/

│   └──evals/


├──  `scripts <https://github.com/bootphon/ABX-accent/tree/main/abx-accent/scripts>`_: Scripts used for the preparation and the evaluation of the data.
│   └──prepare/
│   └──evals/

License
========

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
===========
- Xian Shi, Fan Yu, Yizhou Lu, Yuhao Liang, Qiangze Feng, Daliang Wang, Yanmin Qian, and Lei Xie, “The accented english speech recognition challenge 2020:
  open datasets, tracks, baselines, results and methods,” in ICASSP 2021-2021 IEEE International Conference on Acoustics, Speech and Signal Processing       (ICASSP).IEEE, 2021, pp. 6918–6922.
  



