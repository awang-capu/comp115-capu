# Right click file -> copy path: Absolute file path
# Relative file path
import re

file_r = open("file_data.txt", 'r')
#file_r = open("./lab9/comp115.txt", 'r')

# A line of a file: a string ending with newline character '\n'
for line in file_r:
    print(line)
    #print(repr(line))

    # list_words = line.split()
    # print(list_words)

    # real_words = re.findall(r'\b\w+\b', line)
    # print(real_words)

file_r.close()