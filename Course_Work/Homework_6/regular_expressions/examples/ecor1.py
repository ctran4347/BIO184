import re
dna = "ATCGCGAATTCAC"
if re.search(r"GAATTC", dna):
	print("restriction site found!")
