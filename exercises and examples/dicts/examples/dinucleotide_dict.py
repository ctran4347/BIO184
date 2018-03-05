dna = "AATGATGAACGAC"
dinucleotides = ['AA','AT','AG','AC',
                 'TA','TT','TG','TC',
                 'GA','GT','GG','GC',
                  'CA','CT','CG','CT']
all_counts = {}
for dinucleotide in dinucleotides:
    count = dna.count(dinucleotide)
    print("count is " + str(count) + " for " + dinucleotide)
    all_counts[dinucleotide] = count
print(all_counts)
