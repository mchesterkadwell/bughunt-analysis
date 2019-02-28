import os
import re
from pathlib import Path

# Prepare input and output file paths
data_in = os.path.join('corpora', 'bughunt', '1-initial-manual-clean')
data_out = os.path.join('corpora', 'bughunt', '2-clean-by-decade')

# Create list of input files from whatever is in the data_in directory
files_in = [os.path.join(path, filename)
             for path, _, files in os.walk(data_in)
             for filename in files]

# Create output files in decades
decades = [decade for decade in range(1800, 1920, 10)]
files_out = [os.path.join(data_out, f'bughunt-clean-{decade}.txt') for decade in decades]
for f_out in files_out:
    Path(f_out).touch(exist_ok=True)

# Create dictionary of input file with corresponding decade output file
files = {}
for file_in in files_in:
    # Find the year of the text
    year = re.findall(r'\d{4}', file_in)[0]
    # Decade of that year
    decade = year[0:3] + '0'
    # Find the right output file
    file_out = ''
    for f_out in files_out:
        if re.search(decade, f_out):
            file_out = f_out
            break
    files[file_in] = file_out

# Append each file to the appropriate decade file
count = 1
for file_in in files:
    with open(file_in, 'r', encoding='utf8') as reader, open(files[file_in], 'a', encoding='utf8') as writer:
            print(f'{count}: WRITING {file_in} TO {files[file_in]}')
            writer.write(reader.read())
            count += 1

