#AT Content
#Given short dna sequence
# Calculate AT content
short_dna_sequence_content = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
dna_length=len(short_dna_sequence_content) # determines length of dna sequence or a string
a_count=short_dna_sequence_content.count("A") #counts the number of A's in the strng
t_count=short_dna_sequence_content.count("T") #counts the number of T's in the string
a_t_content=((a_count + t_count)/dna_length)
percentage=(100*a_t_content)
print("The a_t_content in the dna sequence",a_t_content,"\nOr the percentage of at in the sequence is",percentage)

#Complementing DNA
#Given short dna sequence & knowledge of respective base pairs
# Print the complement of this sequence
short_dna_sequence_compliment="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
short_dna_sequence_1=short_dna_sequence_compliment.replace('G','C') # rE
short_dna_sequence_2=short_dna_sequence_1.replace('C','G')
short_dna_sequence_3=short_dna_sequence_2.replace('A','T')
short_dna_sequence_final=short_dna_sequence_3.replace('T','A')
print("The complimentary dna sequence is",short_dna_sequence_final)

#Restriction fragment lengths
#Given short dna sequence, two exons & intron.
#Exon from start to 63, Second exon from 93 to end
#Write a program which will calculate the size of the two fragments that will be produced when the DNA is digested with EcoRI\
#Cuts at the motif G*ATTC
short_dna_sequence_fragment ="ACTGATCGATTACGTATAGTAG*AATTCTATCATACATATATATCGATGCGTTCAT"
split=short_dna_sequence_fragment.find("*") #.find searches for the index at which said string is located
fragment_1=short_dna_sequence_fragment[:split] #prints the start to said index
fragment_2=short_dna_sequence_fragment[split+1:] #prints from said index to the end of the total index
print("Fragment on the left is ",fragment_1)
print("Fragment on the right is ",fragment_2)

#Splicing out introns, part one
#Given short section of genomic DNA
#Write a program that will print just the coding regions of the DNA sequence
short_dna_sequence_splicing_intron_1="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon_1_1=short_dna_sequence_splicing_intron_1[:63]
exon_1_2=short_dna_sequence_splicing_intron_1[93:]
intron_1_1=short_dna_sequence_splicing_intron_1[64:92]
print("Exon 1 is", exon_1_1)
print("Exon 2 is", exon_1_2)
print("Intron 1",intron_1_1)

#Splicing out Introns 2
#Given data from part one
# Write a program that will calculate what percentage of the DNA sequence is coding

len_exon_1_1=len(exon_1_1)
len_exon_1_2=len(exon_1_2)
len_intron_1_1=len(intron_1_1)
whole_dna_sequence_splicing_2=(len_exon_1_1+len_exon_1_2+len_intron_1_1)
dna_sequence_coding_region=(len_exon_1_1+len_exon_1_2)
decimal_coding_region=((dna_sequence_coding_region)/whole_dna_sequence_splicing_2)
percentage_coding_region=100*decimal_coding_region
print("The percentage of DNA that is actually coding is", percentage_coding_region)

#Splicing out introns, part three
#Given data part one
print("The revised dna sequence has been changed so that the coding bases are upper and non-coding are lower cased:",short_dna_sequence_splicing_intron_1[:63] + short_dna_sequence_splicing_intron_1[64:92].lower() + short_dna_sequence_splicing_intron_1[93:])