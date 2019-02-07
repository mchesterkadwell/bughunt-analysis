import os
import re

from nltk.corpus.reader import PlaintextCorpusReader, WordListCorpusReader
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.probability import FreqDist

import pandas as pd
import matplotlib.pyplot as plt

# Create list of files to be read
data_path = os.path.join('nltk_data', 'corpora', 'msbooks')
files = [os.path.join(root, filename) for root, _, files in os.walk(data_path) for filename in files]

# Create a corpus reader with all the files
reader = PlaintextCorpusReader('.', files)

# Get a list of English stopwords
english_stops = set(stopwords.words('english'))

# Load the insect wordlist
insect_words = WordListCorpusReader('.', ['insect-wordlist.txt'])

freq_data = []

# Read each file in turn
for file in files:
    text = reader.raw(file)

    # Tokenise into words
    words = word_tokenize(text)

    # Remove stopwords from the tokens
    words_nostops = [word for word in words if word not in english_stops]

    # Create a frequency distribution from the samples (words)
    freqdist = FreqDist(words_nostops)

    # Create a dict with the frequency of the insect words only
    insect_freq = {word: freqdist.freq(word) for word in insect_words.words()}

    # Add the year from the file name to the dict
    year = re.findall(r'\d{4}', file)
    insect_freq['year'] = year[0]

    # Add the results from this file to the total results
    freq_data.append(insect_freq)

# Create a Pandas DataFrame
df = pd.DataFrame(freq_data)

# Create and save a plot
ax = plt.gca()
for insect in insect_words.words():
    df.plot(kind='line', x='year', y=insect, ax=ax)
plt.xlabel('year')
plt.ylabel('frequency of insect word')
plt.savefig('insect-figs/insect-freq-unigram.png')

# Export the results to CSV
df.to_csv('insect-data/insect-freq-unigram.csv', index=False)


