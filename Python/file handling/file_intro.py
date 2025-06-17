xfile = open('Data_Engineer\\Python\\file handling\\basic_structure_of_file_handling.txt')
# print(xfile.read())

# how many lines in the file
count = 0
for line in xfile:
    count += 1
print('lines:', count)

# print the selected lines
xfile.seek(0)  # reset the file pointer to the beginning
print('first line:', xfile.readline().strip())

# print the characters in the file
char_count = len(xfile.read())
print('characters:', char_count)

# print the lines in the file
xfile.seek(0)  # reset the file pointer to the beginning
lines = xfile.readlines()
for line in lines:
    if line.startswith('mode'):
        print('line:', line.strip())
# print('lines:', lines.start)