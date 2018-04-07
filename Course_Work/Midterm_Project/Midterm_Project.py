
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
    gc_content=((g_content+c_content)/(length))*100
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

first_sequence=sequence_only[0]
second_sequence=sequence_only[1]
third_sequence=sequence_only[2]

# Counts how many restriction sites there are for NcoI, for reference
# ncoi_total=0
# for lines in sequence_only: # Counts the number of NcoI restriction sites
#     ncoi_count=lines.count("CCATGG")
#     ncoi_total += ncoi_count
#     print("NcoI count is",ncoi_count)
# print("NcoI total is",ncoi_total)

def sorting_by_length(genomic_sequence): # Sorts by length
    #Definition created to sort a genomic sequence by length
    genomic_sequence.sort(key=len)
    return(genomic_sequence)

first_sequence_placeholder_1=[]
first_sequence_placeholder_2=[]
 # splits restriction sites and adds nucleotides back
if first_sequence.count("CCATGG") != 0:
    split=first_sequence.split("CCATGG")
    split_1=split[0] + str("C")
    split_2= str("CATGG") + split[1]    
    first_sequence_placeholder_1.append(split_1)
    first_sequence_placeholder_1.append(split_2)
else:
    pass

for splices in first_sequence_placeholder_1:
    if splices.count("GAGCTC") !=0:
        split=splices.split("GAGCTC")
        split_1=split[0]+str("GAGCT")
        split_2= str("C") + split[1]
        first_sequence_placeholder_2.append(split_1)
        first_sequence_placeholder_2.append(split_2)
    else:
        first_sequence_placeholder_2.append(splices)

first_sequence_sorted=sorting_by_length(first_sequence_placeholder_2) 
first_sequence_sorted_reverse=first_sequence_sorted.reverse() # Reverse the list so that the largest fragment is first

output3=open("splicings_sorted_by_length_first_sequence.txt","w")
for lines in first_sequence_sorted: # Checks whether the method above works
    print("Length is" + "\t" + str(len(lines)) + "\t" + lines)
    output3.write("Length is" + "\t" + str(len(lines)) + "\t" + lines + "\n")

largest_fragment_first=first_sequence_sorted[0] # Theoretically largest element should be first
vector=open("pTrc99A.txt").read().replace(">pTrc99A","").upper()
vector_file_1=vector[1:].replace("\n","")

if vector_file_1.count("CCATGG") != 0:
    vector_ncoi_cut_1=vector_file_1.replace("CCATGG",largest_fragment_first) # Replaces every NcoI site with the largest fragment
else:
    print("No NcoI restriction sites")


if vector_ncoi_cut_1.count("GAGCTC") != 0:
    final_vector_1=vector_ncoi_cut_1.replace("GAGCTC",largest_fragment_first) # Replaces every SacI site with the largest fragment
else:
    print("No SocI restriction sites")

print("The Final Vector is",final_vector_1)
output4=open("final_vector_1.txt","w").write(">pTrc99A" + "\n" + final_vector_1)


 # SECOND SEQUENCE
second_sequence_placeholder_1=[]
second_sequence_placeholder_2=[]
 # splits restriction sites and adds nucleotides back
if second_sequence.count("CCATGG") != 0:
    split=second_sequence.split("CCATGG")
    split_1=split[0] + str("C")
    split_2= str("CATGG") + split[1]    
    second_sequence_placeholder_1.append(split_1)
    second_sequence_placeholder_1.append(split_2)
else:
    pass

for splices in second_sequence_placeholder_1:
    if splices.count("GAGCTC") !=0:
        split=splices.split("GAGCTC")
        split_1=split[0]+str("GAGCT")
        split_2= str("C") + split[1]
        second_sequence_placeholder_2.append(split_1)
        second_sequence_placeholder_2.append(split_2)
    else:
        second_sequence_placeholder_2.append(splices)
print(second_sequence_placeholder_2)
second_sequence_sorted=sorting_by_length(second_sequence_placeholder_2) 
second_sequence_sorted_reverse=second_sequence_sorted.reverse() # Reverse the list so that the largest fragment is first

output5=open("splicings_sorted_by_length_second_sequence.txt","w")
for lines in second_sequence_sorted: # Checks whether the method above works
    print("Length is" + "\t" + str(len(lines)) + "\t" + lines)
    output5.write("Length is" + "\t" + str(len(lines)) + "\t" + lines + "\n")

largest_fragment_second=second_sequence_sorted[0] # Theoretically largest element should be first
vector=open("pTrc99A.txt").read().replace(">pTrc99A","").upper()
vector_file_2=vector[1:].replace("\n","")

if vector_file_2.count("CCATGG") != 0:
    vector_ncoi_cut_2=vector_file_2.replace("CCATGG",largest_fragment_second) # Replaces every NcoI site with the largest fragment
else:
    print("No NcoI restriction sites")


if vector_ncoi_cut_2.count("GAGCTC") != 0:
    final_vector_2=vector_ncoi_cut_2.replace("GAGCTC",largest_fragment_second) # Replaces every SacI site with the largest fragment
else:
    print("No SocI restriction sites")

print("The Final Vector is",final_vector_2)
output6=open("final_vector_2.txt","w").write(">pTrc99A" + "\n" + final_vector_2)

# Third sequence
third_sequence_placeholder_1=[]
third_sequence_placeholder_2=[]
 # splits restriction sites and adds nucleotides back
if third_sequence.count("CCATGG") != 0:
    split=third_sequence.split("CCATGG")
    split_1=split[0] + str("C")
    split_2= str("CATGG") + split[1]    
    third_sequence_placeholder_1.append(split_1)
    third_sequence_placeholder_1.append(split_2)
else:
    pass

for splices in third_sequence_placeholder_1:
    if splices.count("GAGCTC") !=0:
        split=splices.split("GAGCTC")
        split_1=split[0]+str("GAGCT")
        split_2= str("C") + split[1]
        third_sequence_placeholder_2.append(split_1)
        third_sequence_placeholder_2.append(split_2)
    else:
        third_sequence_placeholder_2.append(splices)
print(third_sequence_placeholder_2)
third_sequence_sorted=sorting_by_length(third_sequence_placeholder_2) 
third_sequence_sorted_reverse=third_sequence_sorted.reverse() # Reverse the list so that the largest fragment is first

output7=open("splicings_sorted_by_length_third_sequence.txt","w")
for lines in third_sequence_sorted: # Checks whether the method above works
    print("Length is" + "\t" + str(len(lines)) + "\t" + lines)
    output7.write("Length is" + "\t" + str(len(lines)) + "\t" + lines + "\n")

largest_fragment_third=third_sequence_sorted[0] # Theoretically largest element should be first
vector=open("pTrc99A.txt").read().replace(">pTrc99A","").upper()
vector_file_3=vector[1:].replace("\n","")

if vector_file_3.count("CCATGG") != 0:
    vector_ncoi_cut_3=vector_file_3.replace("CCATGG",largest_fragment_third) # Replaces every NcoI site with the largest fragment
else:
    print("No NcoI restriction sites")


if vector_ncoi_cut_3.count("GAGCTC") != 0:
    final_vector_3=vector_ncoi_cut_3.replace("GAGCTC",largest_fragment_third) # Replaces every SacI site with the largest fragment
else:
    print("No SocI restriction sites")

print("The Final Vector is",final_vector_3)
output8=open("final_vector_3.txt","w").write(">pTrc99A" + "\n" + final_vector_3)








    




