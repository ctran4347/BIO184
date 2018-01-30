#Splicing out introns, part one
#First exon runs from the start of the sequence to the sixty-third (Character 1-63)
#Second exon runs from ninety-first to the end of the sequence (Character 91-end)
# Intron is everything else (64-90)
#Given short section of genomic DNA
#Write a program that will print just the coding regions of the DNA sequence
short_dna_sequence_splicing_intron="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon_1=short_dna_sequence_splicing_intron[:62] #Creates variable of start index (0),1st character to desired index(62) or character 63. This means that it takes characters 1-63, but not including 63 or index 63. Because it is exlusive. Math: [1:62)
exon_2=short_dna_sequence_splicing_intron[90:] # Creates variable of index 90 or 91st character to the very end index. The exclusive rule does not apply and does not exclude the last index.
intron_1=short_dna_sequence_splicing_intron[63:90] # Creates variable of index 63 or character 64 to index 89 or character 90 and does not include index 91 or 90. Because it is exlusive and does not include 91. In math, itd be [63,90) in terms of characters. In terms of index , it'd be
#print("Exon 1 is from start of sequence to the sixty-third character is", exon_1)
#print("Exon 2 is from 91 character to the end of the sequence", exon_2)
#print("Intron 1 is from the 64th character to the 90th character because math",intron_1)
print("Coding regions of the DNA sequence is",exon_1 + exon_2)