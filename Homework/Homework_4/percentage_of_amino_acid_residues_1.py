def get_aa_percentage_1(amino_sequence,amino_acid):
    amino_sequence=amino_sequence.upper() #Capitalizes string just in case 
    amino_acid=amino_acid.upper() #Capitalizes string to match for .count()
    amino_sequence_length=len(amino_sequence)
    amino_acid_count=amino_sequence.count(amino_acid)
    percentage=((amino_acid_count)/(amino_sequence_length))*100
    return percentage
assert get_aa_percentage_1("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert get_aa_percentage_1("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert get_aa_percentage_1("msrslllrfllfllllpplp", "L") == 50
assert get_aa_percentage_1("MSRSLLLRFLLFLLLLPPLP", "Y") == 0
