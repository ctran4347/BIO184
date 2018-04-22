import os,re, sys
#---------------------------------
#Clears screen
os.system("clear")
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

# class DNARecord(object):
#     def __int__(self,species_name,group_number,sequence):
#         self.species_name=species_name  
#         self.group_number=group_number

def translation(self):
    protein = ""
    last_codon = len(self) - 2
# Iterates starting at 0 and increases by 3 indexes each time
    for start_position in range(0, last_codon, 3):
        current_codon = self[start_position:start_position + 3]
        amino_acid = genecode.get(current_codon, "X")
        protein += amino_acid
    return protein
#--------------------------------
species_name=[]
group_number=[]
translated_sequeunce=[]
for entry in open("multi-species_alignments.fa"):
    if entry.startswith(">"):
        split=entry.strip("\n").split("\t")
        species_name.append(split[0])
        group_number.append(split[1])
    else:
        translated_sequeunce.append(translation(entry))
print(species_name)
