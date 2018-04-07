def get_aa_percentage_2(dna_sequence,amino_acid_list=["A","I","L","M","F","W","Y","V"]):
    dna_sequence_length=len(dna_sequence)
    dna_sequence=dna_sequence.upper()
    total_percentage=0
    for amino_acids in amino_acid_list:
        amino_acids=amino_acids.upper()
        amino_acids_count=dna_sequence.count(amino_acids)
        percentage=(amino_acids_count*100)/(dna_sequence_length)
        total_percentage += percentage
    return total_percentage
assert get_aa_percentage_2("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert get_aa_percentage_2("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert get_aa_percentage_2("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert get_aa_percentage_2("MSRSLLLRFLLFLLLLPPLP") == 65
