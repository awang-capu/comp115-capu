import re

with (
    open('file_data.txt', "r") as infile_ref,
    open('file_data_processed.txt', 'w') as outfile_ref
):
    for line in infile_ref:
        real_words = re.findall(r'\b\w+\b', line)
        for word in real_words:
            outfile_ref.write(f'{word}\n')