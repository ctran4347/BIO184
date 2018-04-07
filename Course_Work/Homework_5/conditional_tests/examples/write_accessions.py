file1 = open("one.txt", "w")
file2 = open("two.txt", "w")
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
	if accession.startswith('a'):
		file1.write(accession + "\n")
	else:
		file2.write(accession + "\n")
