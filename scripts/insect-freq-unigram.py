import os
import re
import string
from datetime import datetime
from time import time

from nltk.corpus.reader import PlaintextCorpusReader, WordListCorpusReader
from nltk.corpus import stopwords
from nltk import word_tokenize, PorterStemmer
from nltk.probability import FreqDist

import pandas as pd
import matplotlib.pyplot as plt

start = time()
now = datetime.now()
print(f'Started at {now}...')

# Create list of files to be read
data_path = os.path.join('corpora', 'bughunt', '2-clean-by-decade')
files = [os.path.join(root, filename) for root, _, files in os.walk(data_path) for filename in files]

# Create a corpus reader with all the files
reader = PlaintextCorpusReader('.', files)

# Set up a translation table for punctuation to the empty string
table = str.maketrans('', '', string.punctuation)

# Get a list of English stopwords without punctuation
english_stops = set(stopwords.words('english'))
english_stops_nopunct = {stopword.translate(table) for stopword in english_stops}

# Load the insect wordlist of stems
insect_words = WordListCorpusReader('.', ['wordlists/insect-wordstems.txt'])

# A list to hold the frequency data
freq_data = []

count = 1
# Read each file in turn
for file in files:
    text = reader.raw(file)

    print(f'{count}: TOKENISING {file}')

    # Tokenise and normalise to lowercase
    tokens = word_tokenize(text.lower())

    # Remove all punctuation marks
    tokens_nopunct = [token.translate(table) for token in tokens]

    # Remove all tokens that are only numbers (or punctuation marks if there were any left)
    words = [word for word in tokens_nopunct if word.isalpha()]

    # Remove stopwords from the tokens
    words_nostops = [word for word in words if word not in english_stops_nopunct]

    # Stem the words
    porter = PorterStemmer()
    stems = [porter.stem(word) for word in words_nostops]

    # Create a frequency distribution from the samples (words)
    freqdist = FreqDist(stems)

    # Create a dict with the frequency of the insect words only
    insect_freq = {word: freqdist.freq(word) for word in insect_words.words()}

    # Add the year from the file name to the dict
    year = re.findall(r'\d{4}', file)
    insect_freq['year'] = year[0]

    # Add the results from this file to the total results
    freq_data.append(insect_freq)

    count += 1

# Create a Pandas DataFrame
df = pd.DataFrame(freq_data)

print('PLOTTING...')

# Create and save a plot
ax = plt.gca()
for insect in insect_words.words():
    df.plot(kind='line', x='year', y=insect, ax=ax)
plt.xlabel('year')
plt.ylabel('frequency of insect word')
plt.savefig('output/figs/bughunt/insect-stem-freq-unigram.png')

# Export the results to CSV
df.to_csv('output/csv/bughunt/insect-stem-freq-unigram.csv', index=False)

finish = time()
timing = round(finish - start)
now = datetime.now()
print(f'Finished at {now}. Took {timing} seconds.')


