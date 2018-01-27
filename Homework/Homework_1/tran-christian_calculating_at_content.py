#AT Content
#Given short dna sequence
# Calculate AT content
short_dna_sequence_content = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
dna_length=len(short_dna_sequence_content) # determines length of dna sequence or a string
a_count=short_dna_sequence_content.count("A") #counts the number of A's in the strng
t_count=short_dna_sequence_content.count("T") #counts the number of T's in the string
a_t_content=((a_count + t_count)/dna_length) # determines the AT content in said DNA length
percentage=(100*a_t_content) # calculates the percentage
print("The a_t_content in the dna sequence",a_t_content,"or the percentage of at in the sequence is",percentage)
