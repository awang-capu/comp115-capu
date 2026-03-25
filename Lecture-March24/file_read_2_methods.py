file_ref = open("file_data.txt", 'r')

first_line = file_ref.readline()
print(first_line)
#print(repr(first_line))

# lines = file_ref.readlines() # a list of strings
# print(lines)

#st = file_ref.read() # a string

file_ref.close()

