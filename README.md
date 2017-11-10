# ParkinsonDream
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
# mPower feature extraction for Parkinson's disease DREAM challenge
This repository contains code for automatically extracting features that
are predictive of Parkinson's disease using deep learning.
We validated our method in the [Parkinson's disease digital biomarker DREAM challenge](https://www.synapse.org/#!Synapse:syn8717496/wiki/).
For a summary of our approach please can be found [here](https://www.synapse.org/#!Synapse:syn10911551/wiki/470623).
## Requirements
To run the scripts you need the following software requirements:
1. Install [Anaconda2-4.4.0](https://www.continuum.io/downloads). 

Subsequently, the necessary requirements can be installed using
 `conda create --name <env> --file requirements.txt`

## Environment variables
You need to set the environment variable `PARKINSON_DREAM_DATA` to point to
the directory where the dataset should be stored. For instance,
on Linux use 

`export PARKINSON_DREAM_DATA=/path/to/data/`


## Training

The individual models are pre-trained on the specified dataset according to
```
cd <repo_root>/code

# Pre-training for submission_v1.csv
python run_all.py -df svdrotout -mf conv3l_30_300_10_20_30_10_10 --rofl
python run_all.py -df flprotres -mf conv2l_30_300_10_20_30 --rofl
python run_all.py -df rrotret -mf conv2l_30_300_10_20_30 --rofl
python run_all.py -df fbpwcuaout -mf conv3l_30_300_10_40_30_10_10 --rofl
python run_all.py -df fbpwcuaout -mf conv2l_30_300_10_20_30 --rofl
python run_all.py -df svduaret -mf conv2l_30_300_10_20_30 --rofl

# Pre-training for submission_v2.csv
python run_all.py -df svdrotout -mf conv2l_30_300_10_40_30 --rofl
python run_all.py -df flprotres -mf conv2l_30_300_10_40_30 --rofl
python run_all.py -df rrotret -mf conv2l_30_300_10_20_30 --rofl
python run_all.py -df fhpwcuaout -mf conv3l_50_300_10_20_30_10_10 --rofl
python run_all.py -df fbpwcuaout -mf conv2l_50_300_10_40_30 --rofl
python run_all.py -df fhpwcuaout -mf conv2l_30_300_10_40_30 --rofl
```
These commands will also automatically download and preprocess the mPower.

For submission_v2.csv, an integration model was used that used the top-level
feature activities from the pre-trained models as input for neural network
consisting of two layers. The integraion model was trained using

```
python merge_classifier.py alldata.integration1
```

## Feature prediction

Finally, the feature predictions were generated using
```
python featurizer.py --genfeat1 --genfeat2
```
