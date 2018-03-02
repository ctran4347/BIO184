my_file = open("dna.txt")
my_file_contents = my_file.read()
# remove the newline from the end of the file contents
my_dna = my_file_contents.rstrip("\n")
dna_length = len(my_dna)
print("sequence is " + my_dna +  " and length is " + str(dna_length))
