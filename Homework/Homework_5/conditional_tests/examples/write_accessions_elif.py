file1 = open("one.txt", "w")
file2 = open("two.txt", "w")
file3 = open("three.txt", "w")
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
	if accession.startswith('a'):
		file1.write(accession + "\n")
	elif accession.startswith('b'):
		file2.write(accession + "\n")
	else:
		file3.write(accession + "\n")
