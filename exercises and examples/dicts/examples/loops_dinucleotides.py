dna = "AATGATGAACGAC"
bases = ['A','T','G','C']
all_counts = {}
for base1 in bases:
    for base2 in bases:
        dinucleotide = base1 + base2
        count = dna.count(dinucleotide)
        if count > 0:
            all_counts[dinucleotide] = count
