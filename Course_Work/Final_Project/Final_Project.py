import os,re, sys
#---------------------------------
#Clears screen
os.system('clear')
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
<<<<<<< HEAD
#--------------------------------
class DNARecord:
    def __int__(self,file_name):
        self.file_name=file_name
    def header(self)
        for lines in open(file_name):
            if lines.startswith(">")
                split=lines.strip("\n").split("\t")
                header=split[0]
            print(header)


                
=======
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
        self.file_name=file_name    
    def species_name(self):
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
        group_list=[]
        for line in open(self.file_name):
            if line.startswith(">"):
                split=line.strip("\n").split("\t")
                group_list.append(split[1])
            else:
                pass
        return group_list
    def sequence(self):
        sequence_list=[]
        temporary_sequence_string = ""
        for line in open(self.file_name):
            if line.startswith(">"):
                sequence_list.append(temporary_sequence_string)
                temporary_sequence_string = ""
            else:
                temporary_sequence_string += line.strip()
        return sequence_list
#--------------------------------------
d1=DNARecord("multi-species_alignments.fa")
print(d1.sequence())
def compare(str1,str2):
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
    if name.startswith(">Hs"):
        human_name=name
        human_group_number=group
        human_sequence=sequence
        test_list.append(human_sequence)
    else: 
        temp_name_list.append(name) # species name
        temp_group_list.append(group) # group number
        temp_sequence_list.append(sequence) # sequence
    if group not in test_dict.keys():
        test_dict[group]= 1
    elif group in test_dict.keys():
        test_dict[group] += 1
    if test_dict.get(group) == 5:
        for name,sequeunce in zip(temp_name_list,temp_sequence_list):
            translated_human_sequence=translation(human_sequence)
            translated_sequeunce=translation(sequence)
            similarity=compare(translated_human_sequence,translated_sequeunce)
            if name not in similarity_dict.keys(): # iterates 4 times
                similarity_dict[name]=[]
                similarity_dict[name].append(similarity)
            elif name in similarity_dict.keys(): # its 96 times
                similarity_dict[name].append(similarity)
        temp_name_list=[]
        temp_group_list=[]
        temp_sequence_list=[]
        human_name=""
        human_group_number=""
        human_sequence=""
    else:
        pass
>>>>>>> ad85a3b1a2dd0629e1df80d26132d88c51a41f70

# -------------------------------------
# for name,similarity in similarity_dict.items():
#     true_average= sum(similarity) / float(len(similarity))
#     print(name,"\n",true_average)