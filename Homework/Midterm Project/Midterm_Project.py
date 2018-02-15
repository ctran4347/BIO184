# Midterm Project part one
count=0 #just for testing purposes
sequence_file=open("sequences.txt") # Sequence file is opened
sequence=sequence_file.read() # Sequence file is read
removed_lines=sequence.replace(" ","") # White space is removed
name_and_sequence=removed_lines.split() # the names and sequence split into a list
sequence_only=name_and_sequence[1::2] # Sorts list to remove headers at the beginning of every odd line
output1=open("dna_sequence_by_length.txt","w") 
output2=open("dna_sequence_by_gc_content.txt","w")



def sorting_by_length(genomic_sequence): # Sorts by length
    #Definition created to sort a genomic sequence by length
    genomic_sequence.sort(key=len)
    return(genomic_sequence)
print(">Sorted List by Length")

dna_sequence_length=sorting_by_length(sequence_only) # 

for lines in dna_sequence_length: # Goes through each line in file and sorts by length
    print("*Length =",len(lines),lines,"\n")  # Goes through each element(lines) in file
    length=str(len(lines))
    output1.write(length + "\n" + lines + "\n") # Writes the output and made pretty

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
    output2.write(gc_content + "\n" + lines + "\n")  # Writes output and made pretty    

#Midterm Project Part 2
# NcoI cleaves at 5' C^CATGG 
# SacI cleaves at 5' GAGCT^C

# Counts how many restriction sites there are for NcoI, for reference
ncoi_total=0
for lines in sequence_only: # Counts the number of NcoI restriction sites
    ncoi_count=lines.count("CCATGG")
    ncoi_total += ncoi_count
    print("NcoI count is",ncoi_count)
print("NcoI total is",ncoi_total)


ncoi_list=[]
for lines in sequence_only: # splits restriction sites and adds nucleotides back
    if lines.count("CCATGG") != 0:
        split=lines.split("CCATGG")
        split_1=split[0] + str("C")
        split_2= str("CATGG") + split[1]    
        ncoi_list.append(split_1)
        ncoi_list.append(split_2)
    else:
        pass
print(type(sequence_only))
print(type(ncoi_list))

#Counts the number of SacI restriction sites for reference
saci_total=0
for lines in ncoi_list: # Counts the number of SacI restriction sties
    saci_count=lines.count("GAGCTC")
    saci_total += saci_count
    print("SacI count is",saci_count)
print("SacI total is",saci_total)

saci_list=[]
for lines in ncoi_list: # splits restriction sites and adds nucleotides back
    if lines.count("GAGCTC") !=0:
        split=lines.split("GAGCTC")
        split_1=split[0]+str("GAGCT")
        split_2= str("C") + split[1]
        saci_list.append(split_1)
        saci_list.append(split_2)
    else:
        pass
print(saci_list)


sorted_restriction_fragments=sorting_by_length(saci_list) # Sorts fragments
sorted_restriction_fragments_reverse=sorted_restriction_fragments.reverse() # Reverse the list so that the largest fragment is first

for lines in sorted_restriction_fragments: # Checks whether the method above works
    print("length is",len(lines),lines)

largest_fragment=sorted_restriction_fragments[0] # Theoretically largest element should be first
vector_file=open("pTrc99A.txt").read().upper()



if vector_file.count("CCATGG") != 0:
    vector_ncoi_cut=vector_file.replace("CCATGG",largest_fragment) # Replaces every NcoI site with the largest fragment
else:
    print("No NcoI restriction sites")


if vector_ncoi_cut.count("GAGCTC") != 0:
    final_vector=vector_ncoi_cut.replace("GAGCTC",largest_fragment) # Replaces every SacI site with the largest fragment
else:
    print("No SocI restriction sites")

print("The Final Vector is",final_vector)
output3=open("final_vector.txt","w").write(final_vector)



    




