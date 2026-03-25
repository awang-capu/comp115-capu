import re

infile_ref = open('file_data.txt', "r")
outfile_ref = open('file_data_processed.txt', 'w') # Create a new file or erase previous data

lines = infile_ref.readlines()
for line in lines:
    real_words = re.findall(r'\b\w+\b', line)
    for word in real_words:
        outfile_ref.write(f'{word}\n')

infile_ref.close()
outfile_ref.close()

