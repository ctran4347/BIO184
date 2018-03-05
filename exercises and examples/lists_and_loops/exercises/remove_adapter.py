# open the input file
file = open("input.txt")

# open the output file
output = open("trimmed.txt", "w")

# go through the input file one line at a time
for dna in file:

    # get the substring from the 15th character to the end
    trimmed_dna = dna[14:]

    # get the length of the trimmed sequence
    trimmed_length = len(trimmed_dna) - 1

    # print out the trimmed sequence
    output.write(trimmed_dna)

    # print out the length to the screen
    print("processed sequence with length " + str(trimmed_length))
