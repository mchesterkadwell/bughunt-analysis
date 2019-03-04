#Bughunt!

##Introduction

This repository contains scripts and Jupyter notebooks for *Bughunt! 2019*, a 
guided project undertaken by Faculty of Education students as part of the 
Cambridge Digital Humanities Learning programme.
 
The project focuses on the distant reading of English children's literature 
1789-1914 for the representation of insects and other creepy crawlies.

Participants collated and manually cleaned a corpus of out-of-copyright books 
from a number of sources, which may be found in the [1-initial-manual-clean](corpora/bughunt/1-initial-manual-clean)
folder.

##Code details

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

##Getting started

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mchesterkadwell/bughunt-analysis/master)

The easiest way to run the Jupyter notebooks in this repository is to click on 
the Binder button above. This will launch a virtual environment in your 
browser where you can open and run the notebooks without installing anything.

To run the analysis scripts themselves, clone the repository and then run the 
scripts in this order:
* [files-by-decade.py](scripts/files-by-decade.py) - takes the cleaned corpus 
and splits it into files arranged by decade of publication.
* [insect-freq-unigram.py](scripts/insect-freq-unigram.py) - tokenises the 
corpus, runs a frequency distibution and outputs a CSV file of the data and a 
PNG of the data plotted on a line graph.




