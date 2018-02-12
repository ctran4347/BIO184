# Midterm Project part one
count=0 #just for testing purposes
sequence_file=open("sequences.txt") # Sequence file is opened
sequence=sequence_file.read() # Sequence file is read
removed_lines=sequence.replace(" ","") # White space is removed
name_and_sequence=removed_lines.split() # the names and sequence split into a list
sequence_only=name_and_sequence[1::2] # Sorts list to remove headers at the beginning of every odd line
output1=open("dna_sequence_by_length.txt","w") 
output2=open("dna_sequence_by_gc_content.txt","w")



def sorting_by_length(genomic_sequence):
    #Definition create to sort by len
    genomic_sequence.sort(key=len)
    return(genomic_sequence)
print(">Sorted List by Length")
dna_sequence_length=sorting_by_length(sequence_only)
for lines in dna_sequence_length: # Goes through each line in file and sorts by length
    print("*Length =",len(lines),lines,"\n")  # Goes through each element(lines) in file
    length=str(len(lines))
    output1.write(length + "\n" + lines + "\n")

def sorting_gc_content(genomic_sequence):
    # Definition created to find GC content and sort by GC content
    length=len(genomic_sequence)
    g_content=genomic_sequence.count("G")
    c_content=genomic_sequence.count("C")
    gc_content=((g_content+c_content)/(length))
    return gc_content
print(">Sorted List by GC Content")
for lines in sequence_only: # Goes through in each line of file and utilizing sort_gc_content function created
    print("*GC Content =",sorting_gc_content(lines),lines,"\n") 
    gc_content=str(sorting_gc_content(lines))
    output2.write(gc_content + "\n" + lines + "\n")

#Midterm Project Part 2
first_sequence=sequence_only[0]
second_sequence=sequence_only[1]
third_sequence=sequence_only[2]

first_sequence_split=first_sequence.split("CCATGG")
print(first_sequence_split)


# NcoI cleaves at 5' C^CATGG 
# SacI cleaves at 5' GAGCT^C
first_sequence_ncoi_count=first_sequence.count("CCATGG")
second_sequence_ncoi_count=second_sequence.count("CCATGG")
third_sequence_ncoi_count=third_sequence.count("CCATG")
print(first_sequence_ncoi_count,second_sequence_ncoi_count,first_sequence_ncoi_count)
1#NcoI search & split



