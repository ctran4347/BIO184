
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
    print(names + "\t" + str(len( sequences)) + "\t" + sequences + "\n" + "\n")
    output1.write(names + "\t"+ str(len(sequences)) + "\t" + sequences + "\n" + "\n")

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

def randomfunction2(a):
    # Another function that returns the next value. 
    return a[1]

for names,gc_content,sequences in sorted(zip(names_only,gc_content_list,sequence_only),key=randomfunction2):
    print(names + "\t"+ str(gc_content) + "\t" + sequences + "\n" + "\n")
    output2.write(names + "\t" + str(gc_content) + "\t" + sequences + "\n" + "\n")

#Midterm Project Part 2
# NcoI cleaves at 5' C^CATGG 
# SacI cleaves at 5' GAGCT^C


# Counts how many restriction sites there are for NcoI, for reference
# ncoi_total=0
# for lines in sequence_only: # Counts the number of NcoI restriction sites
#     ncoi_count=lines.count("CCATGG")
#     ncoi_total += ncoi_count
#     print("NcoI count is",ncoi_count)
# print("NcoI total is",ncoi_total)

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
# print(type(sequence_only))
# print(type(ncoi_list))

#Counts the number of SacI restriction sites for reference
# saci_total=0
# for lines in ncoi_list: # Counts the number of SacI restriction sties
#     saci_count=lines.count("GAGCTC")
#     saci_total += saci_count
#     print("SacI count is",saci_count)
# print("SacI total is",saci_total)

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
# print(saci_list)

def sorting_by_length(genomic_sequence): # Sorts by length
    #Definition created to sort a genomic sequence by length
    genomic_sequence.sort(key=len)
    return(genomic_sequence)



sorted_restriction_fragments=sorting_by_length(saci_list) # Sorts fragments
sorted_restriction_fragments_reverse=sorted_restriction_fragments.reverse() # Reverse the list so that the largest fragment is first
output3=open("splicings_sorted_by_length.txt","w")
for lines in sorted_restriction_fragments: # Checks whether the method above works
    print("Length is" + "\t" + str(len(lines)) + "\t" + lines)
    output3.write("Length is" + "\t" + str(len(lines)) + "\t" + lines + "\n")

largest_fragment=sorted_restriction_fragments[0] # Theoretically largest element should be first
vector=open("pTrc99A.txt").read().replace(">pTrc99A","").upper()
vector_file=vector[1:].replace("\n","")

if vector_file.count("CCATGG") != 0:
    vector_ncoi_cut=vector_file.replace("CCATGG",largest_fragment) # Replaces every NcoI site with the largest fragment
else:
    print("No NcoI restriction sites")


if vector_ncoi_cut.count("GAGCTC") != 0:
    final_vector=vector_ncoi_cut.replace("GAGCTC",largest_fragment) # Replaces every SacI site with the largest fragment
else:
    print("No SocI restriction sites")

print("The Final Vector is",final_vector)
output4=open("final_vector.txt","w").write(">pTrc99A" + "\n" + final_vector)



    




