# first store a list of lines in the file
file = open("some_input.txt")
all_lines = file.readlines()

# print the lengths
for line in all_lines:
	print("The length is " + str(len(line)))

# print the first characters
for line in all_lines:
	print("The first character is " + line[0])