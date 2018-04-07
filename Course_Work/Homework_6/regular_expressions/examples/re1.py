import re

dna = "CGATGCTGAATTCGACTGC"
if re.search(r"GC[ATGC]GC", dna):
    print("found restriction site!")


