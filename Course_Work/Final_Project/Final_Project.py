import os
import re
import sys

#---------------------------------
#Clears screen
os.system('cls')
#---------------------------------
genecode = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '$', 'TAG': '$',
    'TGC': 'C', 'TGT': 'C', 'TGA': '$', 'TGG': 'W', '---' : "-"}
#--------------------------------------                
def translation(sequence):
    protein = ""
    last_codon = len(sequence) - 2
    # Iterates starting at 0 and increases by 3 indexes each time
    for start_position in range(0, last_codon, 3):
        current_codon = sequence[start_position:start_position + 3]
        amino_acid = genecode.get(current_codon,"")
        protein += amino_acid
    return protein
#-------------------------------------
class DNARecord(object):
    def __init__(self,file_name):
        #constructor function
        self.file_name=file_name    
    def species_name(self):
        #function that seperates species from file 
        species_list=[]
        for line in open(self.file_name):
            if line.startswith(">"):
                split=line.strip("\n").split("\t")
                species_name=split[0]
                cleaned_up=species_name.split("-")
                actual=cleaned_up[0]
                species_list.append(actual)
            else:
                pass
        return species_list
    def group_number(self):
        # function that seperates group number from file
        group_list=[]
        for line in open(self.file_name):
            if line.startswith(">"):
                split=line.strip("\n").split("\t")
                group_list.append(split[1])
            else:
                pass
        return group_list
    def sequence(self):
        # function that seperates sequence from file
        sequence_list=[]
        temporary_sequence_string=""
        for line in open(self.file_name):
            if not line.startswith(">"):
                temporary_sequence_string += line.strip()
            elif line.startswith(">"):
                if sequence_list == []:
                    pass
                sequence_list.append(temporary_sequence_string)        
                temporary_sequence_string=""
        return sequence_list
#--------------------------------------
d1=DNARecord(sys.argv[1])
def compare(str1,str2):
    # Function to compare two strings
    if len(str1) == len(str2):
        max_length=len(str1)
        letters_match=0
        for i in range(0,max_length,1):
            if (str1[i] == str2[i]):
                letters_match += 1
            else:
                pass
    elif len(str1) > len(str2): 
        max_length=len(str2)
        letters_match=0
        for i in range(0,max_length,1):
            if (str1[i] == str2[i]):
                letters_match += 1
            else:
                pass
    elif len(str1) < len(str2): 
        max_length= len(str1)
        letters_match=0
        for i in range(0,max_length,1):
            if (str1[i] == str2[i]):
                letters_match += 1
            else:
                pass
    return letters_match / max_length *100
#---------------------------------------
test_dict={}
temp_name_list=[]
temp_group_list=[]
temp_sequence_list=[]
temp_human_list=[]
similarity_dict={}
human_name=""
human_group_number=""
human_sequence=""
test_list=[]
for name,group,sequence in zip(d1.species_name(),d1.group_number(),d1.sequence()): 
    #Iterates through list of tuples 
    if name.startswith(">Hs"):
        #Checks if tuple starts with >H and sets human variables accordingly
        human_name=name
        human_group_number=group
        human_sequence=sequence
        test_list.append(human_sequence)
    else: 
        #Sets other genes accordingly
        temp_name_list.append(name) # species name
        temp_group_list.append(group) # group number
        temp_sequence_list.append(sequence) # sequence
    if group not in test_dict.keys():
        #Checks whether group has been inputed to dictionary counter. If not creates a new key and value pair
        test_dict[group]= 1
    elif group in test_dict.keys():
        #Checks if group exists in dictionary. If it does, updates value
        test_dict[group] += 1
    if test_dict.get(group) == 5:
        #Checks if value for key is 5 and compares human variables to other gene variables
        for name,sequeunce in zip(temp_name_list,temp_sequence_list):
            translated_human_sequence=translation(human_sequence)
            translated_sequeunce=translation(sequence)
            similarity=compare(translated_human_sequence,translated_sequeunce)
            if name not in similarity_dict.keys(): # iterates 4 times
                similarity_dict[name]=[]
                similarity_dict[name].append(similarity)
            elif name in similarity_dict.keys(): # its 96 times
                similarity_dict[name].append(similarity)
        # Resets lists and variables
        temp_name_list=[]
        temp_group_list=[]
        temp_sequence_list=[]
        human_name=""
        human_group_number=""
        human_sequence=""    
    else:
    # If value for key is not 5. It would continue
        pass
#-------------------------------------
#Prints out average of similarities for each gene.
for name,similarity in similarity_dict.items():
    true_average= sum(similarity) / float(len(similarity))
    print(name,"\n",true_average)
#-------------------------------------
# python3 Final_Project.py multi-species_alignments.fa
