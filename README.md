# Bughunt!

## Introduction

This repository contains scripts and Jupyter notebooks for *Bughunt! 2019*, a 
guided project undertaken by Faculty of Education students as part of the 
Cambridge Digital Humanities Learning programme.
 
The project focuses on the distant reading of English children's literature 
1789-1914 for the representation of insects and other creepy crawlies.

Participants collated and manually cleaned a corpus of out-of-copyright books 
from a number of sources, which may be found in the [1-initial-manual-clean](corpora/bughunt/1-initial-manual-clean)
folder.

## Code details

The aim of the code in this repository is to show basic text mining techniques 
to participants who are complete beginners to both text mining and coding. 
As such, the script code is simple, linear and heavily commented to aid 
understanding, and the notebooks are designed to be run as a teaching aid, not 
to generate analysis results. The notebooks formed the basis of the one of the
workshops held with the group on 5 March 2019.

The main libraries used in this repository are:
* Natural Language Toolkit (NLTK)
* Pandas
* Matplotlib

## Getting started

### Jupyter notebooks

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mchesterkadwell/bughunt-analysis/master)

The easiest way to run the Jupyter notebooks in this repository is to click on 
the Binder button above. This will launch a virtual environment in your 
browser where you can open and run the notebooks without installing anything.

If you want to run the notebooks locally, follow the instructions for cloning 
and installing requirements as in the section below, and then run the notebooks in the way you 
would normally on your machine. (If you are not familiar with Jupyter notebooks 
yet then just use the Binder button to start with.)

There are 3 notebooks under the [notebooks](notebooks) folder:
* [1-intro-to-strings.ipynb](notebooks/1-intro-to-strings.py) - a generic 
introduction to Jupyter notebooks and basic string functions in Python.
* [2-text-processing-corpus.ipynb](notebooks/2-text-processing-corpus.ipynb) - 
a walk through of the principles behind the first part of the script
 [insect-freq-unigram.py](scripts/insect-freq-unigram.py), 
from tokenising the files to generating the frequency distribution.
* [3-visualising-data.ipynb](notebooks/3-visualising-data.ipynb) - a walk 
through of the principles behind the second part of [insect-freq-unigram.py](scripts/insect-freq-unigram.py) 
whereby the basic graph is plotted.

### Analysis scripts

To run the analysis scripts themselves, clone the repository and install the 
required libraries from `requirements.txt`.

`$ pip install -r requirements.txt`

It is strongly recommended that you 
do so in a `venv` virtual environment. (RealPython has an excellent tutorial 
on [virtual environments](https://realpython.com/python-virtual-environments-a-primer/).)

You will also need to download the corpus of stopwords and the punkt tokenizer 
from `nltk_data`. See the official documentation: [Installing NLTK Data](https://www.nltk.org/data.html)

Run the scripts in this order:
* [files-by-decade.py](scripts/files-by-decade.py) - takes the cleaned corpus 
and splits it into files arranged by decade of publication.
* [insect-freq-unigram.py](scripts/insect-freq-unigram.py) - tokenises the 
corpus, runs a frequency distibution and outputs a CSV file of the data and a 
PNG of the data plotted on a line graph.




