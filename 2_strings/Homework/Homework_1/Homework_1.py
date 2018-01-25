#AT Content
#Given short dna sequence
# Calculate AT content
short_dna_sequence_content = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
dna_length=len(short_dna_sequence) # determines length of dna sequence or a string
a_count=short_dna_sequence.count("A") #counts the number of A's in the strng
t_count=short_dna_sequence.count("T") #counts the number of T's in the string
a_t_content=((a_count + t_count)/dna_length)
percentage=(100*a_t_content)
print("The a_t_content in the dna sequence",a_t_content,"\nOr the percentage of at in the sequence is",percentage)
#Complementing DNA
#Given short dna sequence & knowledge of respective base pairs
# Print the complement of this sequence
short_dna_sequence_compliment="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
short_dna_sequence_1=short_dna_sequence.replace('G','C')
short_dna_sequence_2=short_dna_sequence_1.replace('C','G')
short_dna_sequence_3=short_dna_sequence_2.replace('A','T')
short_dna_sequence_final_=short_dna_sequence_3.replace('T','A'
print("The complimentary dna sequence is",short_dna_sequence_final))

#Restriction fragment lengths
#Given short dna sequence
#Write a program which will calculate the size of the two fragments that will be produced when the DNA is digested with EcoRI\
#Cuts at the motif G*ATTC
short_dna_sequence_fragment ="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"


