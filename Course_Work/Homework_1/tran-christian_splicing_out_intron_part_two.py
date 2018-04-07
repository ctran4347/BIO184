
#Splicing out Introns 2
#Given data from part one
# Write a program that will calculate what percentage of the DNA sequence is coding
short_dna_sequence_splicing_intron="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon_1=short_dna_sequence_splicing_intron[:62] #Creates variable of start index (0) or character 1 to desired index (62) or character sixty-three
exon_2=short_dna_sequence_splicing_intron[90:] # Creates variable of index 90 or character 91 to end index
intron_1=short_dna_sequence_splicing_intron[63:89] # Creates variable of end index 63 to 90
len_exon_1=len(exon_1)
len_exon_2=len(exon_2)
len_intron_1=len(intron_1)
whole_dna_sequence_splicing=len(short_dna_sequence_splicing_intron)
dna_sequence_coding_region=(len_exon_1+len_exon_2)
decimal_coding_region=((dna_sequence_coding_region)/whole_dna_sequence_splicing)
percentage_coding_region=100*decimal_coding_region
print("The percentage of DNA that is actually coding is", percentage_coding_region)