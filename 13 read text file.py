# file IO (input/output)

# open file method, name of the file, mode to open
# r = read
# w = write
file = open('file.txt', 'r')

f = file.readlines()
print(f)

newList = []
# iterate through every line in the file
for line in f:
    #newList.append(line[:-1])
    # removes \n
    newList.append(line.strip())

print(newList)
# close file at end of program
file.close()