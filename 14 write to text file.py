# 'w' = write mode
file = open('file.txt', 'w')

# clears entire file and writes text
file.write('python')
# continues writing on same line
file.write('write a new line')
# writes on new line
file.write('\nthis is on a new line')

# close file at end of program
file.close()