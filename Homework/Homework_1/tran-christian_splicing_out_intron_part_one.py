#Splicing out introns, part one
#First exon runs from the start of the sequence to the sixty-third
#Second exon runs from ninety-first to the end of the sequence 
# Intron is everything else
#Given short section of genomic DNA
#Write a program that will print just the coding regions of the DNA sequence
short_dna_sequence_splicing_intron="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon_1=short_dna_sequence_splicing_intron[:62] #Creates variable of start index (0) to desired index(62) or 63rd character
exon_2=short_dna_sequence_splicing_intron[90:] # Creates variable of index 90 or 91st character to end index
intron_1=short_dna_sequence_splicing_intron[63:89] # Creates variable of end index 64 to 90
#print("Exon 1 is from start of sequence to the sixty-third character is", exon_1)
#print("Exon 2 is from 91 character to the end of the sequence", exon_2)
#print("Intron 1 is from the 64th character to the 90th character because math",intron_1)
print("Coding regions of the DNA sequence is",exon_1 + exon_2)