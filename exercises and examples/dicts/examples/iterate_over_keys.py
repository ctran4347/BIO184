dna = "AATGATGAACGAC"
dinucleotides = ['AA','AT','AG','AC',
                 'TA','TT','TG','TC',
                 'GA','GT','GG','GC',
                 'CA','CT','CG','CT']
all_counts = {}
for dinucleotide in dinucleotides:
    count = dna.count(dinucleotide)
    if count > 0:
        all_counts[dinucleotide] = count

for dinucleotide in all_counts.keys():
    if all_counts.get(dinucleotide, 0) == 2:
        print(dinucleotide)
