import re
dna = "ATCGCGAATTCAC"
if re.search(r"GG(A|T)CC", dna):
	print("restriction site found!")
