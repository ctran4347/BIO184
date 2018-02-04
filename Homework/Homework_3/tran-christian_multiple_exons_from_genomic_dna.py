input_file=open("genomic_dna.txt") #Opens the genomic dna file with the given sequence
genomic_section=input_file.read() # Converts text file or rather any file to string. MAKE SURE TO DO THIS OR YOU GET TEXTIOWRAPPER ERRORRRRR
start_stop=open("exons.txt") # Opens given exon start/stop file
coding_sequence="" # This has to be created as a placehold for the for loop to append strings into it
for each_line in start_stop:
    positions=each_line.split(",") #Returns string in list using arguments given
    start=int(positions[0])  # int() converts string into integers. Checks index 0
    stop=int(positions[1])  #Checks index 1
    #print(start,stop) #Good to test whether its been printing/ working.
    exon_segements=genomic_section[start:stop]
    coding_sequence=coding_sequence + exon_segements
#print(coding_sequence) # What this does is that it utilizes coding_sequence("") or an empty string and repeatedly has exon_segments or strings added to it to create the final product
output=open("coding_sequence.txt","w") # Creates an output file in write mode hence the w
output.write(coding_sequence) #Writes into output file with coding_sequence
    