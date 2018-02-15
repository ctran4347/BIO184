def amino_acid_residues_percentage(amino_sequence,amino_acid):
    amino_sequence=amino_sequence.upper() #Capitalizes string just in case 
    amino_acid=amino_acid.upper() #Capitalizes string to match for .count()
    amino_sequence_length=len(amino_sequence)
    amino_acid_count=amino_sequence.count(amino_acid)
    percentage=((amino_acid_count)/(amino_sequence_length))*100
    return percentage
assert amino_acid_residues_percentage("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert amino_acid_residues_percentage("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert amino_acid_residues_percentage("msrslllrfllfllllpplp", "L") == 50
assert amino_acid_residues_percentage("MSRSLLLRFLLFLLLLPPLP", "Y") == 0
