import re
dna = "ATCGCGAATTCAC"
if re.search(r"GC[ATGC]GC", dna):
	print("restriction site found!")
