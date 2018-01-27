#Splicing out introns, part three
#Given data part one
short_dna_sequence_splicing_intron="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

print("The revised dna sequence has been changed so that the coding bases are upper and non-coding are lower cased:",short_dna_sequence_splicing_intron[:62] + short_dna_sequence_splicing_intron[63:89].lower() + short_dna_sequence_splicing_intron[90:])