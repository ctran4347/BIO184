import os,re,sys
def clear():
    return os.system("clear")
clear()

#Creating dictionary for go_terms
input_1= open("go_terms.midterm2.txt").read()
# Removing white sapce
white_space_removed_1=re.split("\t|\n",input_1) 
#Creating empty Lists
go_terms=[] 
go_terms_descriptions=[]
#Separating go terms into a seperate list
for m in range(0,len(white_space_removed_1),2):
    go_terms.append(white_space_removed_1[m])
#Separating go terms desccriptions into a separate list
for n in range(1,len(white_space_removed_1),2):
    go_terms_descriptions.append(white_space_removed_1[n])
# print(go_terms_descriptions)
#Associating the two lists with zip() and creating a dictionary with dict()
dictionary_1=dict(zip(go_terms,go_terms_descriptions))
#Go terms dictionary complete
#---------------------------------------------------------------------------------------
#Gene code taken from homework 6
genecode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W'}
# TAG, TAA, AND TAG are stop codons
#----------------------------------------------------------------------------------------------
# Testing inputs
# input_2=open("transcripts.midterm2.fasta").read()
# white_space_removed_2=re.split("\t|\n",input_2)
# #Creating empty lists
# transcripts=[]
# transcripts_go_terms=[]
# transcripts_sequence=[]
#-----------------------------------------------------------------------------------------------
#Definitions used in the entire project
def translation(sequence):
    protein = ""
    last_codon = len(sequence) -2
    for start_position in range(0,last_codon,3): # Iterates starting at 0 and increases by 3 indexes each time
         current_codon = sequence[start_position:start_position + 3]
         amino_acid=genecode.get(current_codon,"X")
         protein += amino_acid
    return protein
def make_list(n):
    lists=[]
    for derp in range(n):
        lists.append([])
        return lists

#-------------------------------------------------------------------------------------------------
# def main(argv):
transcripts=[] # Used in the final product
transcripts_go_terms=[]
new_go_terms_list=[] # new list blank, used in the final product
transcripts_sequence=[]
new_sequences_list=[] # new list blank, used in the final product 
transcripts_input=open("transcripts.midterm2.fasta").read()
white_space_removed_2=re.split("\t|\n",transcripts_input)
print(len(white_space_removed_2))
    #Separates transcripts into a seperate list
for _ in range(0,len(white_space_removed_2),3):
    transcripts.append(white_space_removed_2[_])
#print(transcripts) # For some reason transcripts hard a blank entry.
new_transcripts=transcripts[:200]
print(new_transcripts)

print(len(transcripts))
    #Seperates trnascript's go terms into a seperate list
for _ in range(1,len(white_space_removed_2),3):
    transcripts_go_terms.append(white_space_removed_2[_])
print(len(transcripts_go_terms))
    #Seperates sequences into a separate list
#print
for _ in range(2,len(white_space_removed_2),3):
    transcripts_sequence.append(white_space_removed_2[_])
print(len(transcripts_sequence))
#--------------------------------------------------------------------------------------------------
#This for loops grabs the description for each go-term and puts it into a list
for go_terms in transcripts_go_terms:
    new_term = dictionary_1.get(go_terms,"No go term description")
    new_go_terms_list.append(new_term)
#--------------------------------------------------------------------------------------------------
#This nested for loop will iterate and translate each sequence within the list of sequences
for sequence in transcripts_sequence:
    new_sequence=translation(sequence)
    new_sequences_list.append(new_sequence)
#---------------------------------------------------------------------------------------------------
list_with_longest_fragment=[]
for new_sequence in new_sequences_list:
    sequence_list=new_sequence.split("*")
    sorted(sequence_list,reverse=True)
    longest_fragment=sequence_list[0]
    list_with_longest_fragment.append(longest_fragment)
print("input_1",input_1)



    



    

        

    


# if __name__ == "__main__":
#     main(sys.argv)
# #--------------------------------------------------------------------------------------------
#If have extra time. Make sys.argv take multiple file inputs


 