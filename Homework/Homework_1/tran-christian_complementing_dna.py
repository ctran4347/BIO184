
#Complementing DNA
#Given short dna sequence & knowledge of respective base pairs
# Print the complement of this sequence
short_dna_sequence_compliment="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
short_dna_sequence_1=short_dna_sequence_compliment.replace('G','1') # Replaces Guanine with respective basepair, Cytosine, but with the placeholder number 1
short_dna_sequence_2=short_dna_sequence_1.replace('C','2') #Replaces Cytosine with respective basepair, Cytosine,but with the placeholder number 2
short_dna_sequence_3=short_dna_sequence_2.replace('A','3') #Replaces Adenine with respective basepair, Cytosine,but with the placeholder number 3
short_dna_sequence_4=short_dna_sequence_3.replace('T','4') #Replaces Thymine with respective basepair, Cytosine,but with the placeholder number 4
short_dna_sequence_5=short_dna_sequence_4.replace('1','C') # Replaces placeholder number 1 with the actual basepair abreviation
short_dna_sequence_6=short_dna_sequence_5.replace('2','G') # Replaces placeholder number 2 with the actual basepair abreviation
short_dna_sequence_7=short_dna_sequence_6.replace('3','T') # Replaces placeholder number 3 with the actual basepair abreviation
short_dna_sequence_final=short_dna_sequence_7.replace('4','A') # Replaces placeholder number 4 with the actual basepair abreviation
print("The complimentary dna sequence for",short_dna_sequence_compliment,"is",short_dna_sequence_final) 