
count=0 #just for testing purposes
sequence_file=open("sequences.txt") # Sequence file is opened
sequence=sequence_file.read() # Sequence file is read
removed_lines=sequence.replace(" ","") # White space is removed
name_and_sequence=removed_lines.split() # the names and sequence split into a list
sequence_only=name_and_sequence[1::2] # Sorts list to remove headers at the beginning of every odd line
output1=open("dna_sequence_by_length.FASTA","w") 
output2=open("dna_sequence_by_gc_content.FASTA","w")
names_only=name_and_sequence[0::2]

def randomfunction(a):
    # Function that returns the next variable
    return len(a[1])

for names,sequences in sorted(zip(names_only,sequence_only),key=randomfunction): 
    print(names,len(sequences),sequences)

def sorting_gc_content(genomic_sequence):
    # Function created to find GC content of a sequence. DOES NOT SORT despite the name
    length=len(genomic_sequence)
    g_content=genomic_sequence.count("G")
    c_content=genomic_sequence.count("C")
    gc_content=((g_content+c_content)/(length))
    return gc_content

gc_content_list=[]
for sequence in sequence_only:
    gc=sorting_gc_content(sequence)
    gc_content_list.append(gc)
print(gc_content_list)

def randomfunction2(a):
    # Another function that returns the next value. 
    return a[1]

for names,gc_content,sequences in sorted(zip(names_only,gc_content_list,sequence_only),key=randomfunction2):
    print(names,gc_content,sequences)