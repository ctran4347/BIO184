# Matlab's equivalent of clear/clc
import os


# Mac's version is clear and Windows is cls
def clear(): return os.system("clear")


clear()

# Opens and reads DNA file and gets rid of white space because we know that this contains a dna sequence
dna_sequence = open("dna.txt").read().strip("\n")

import re
# 0 is to indicate the start of the sequence to consider in creating fragments.
cuts_list = [0]
# This iterates through a given string or list. The cut is at A[ATGC]T^AAT. The cut is at index 3 or character 4.
for AbcI_match in re.finditer(r"A[AGCT]TAAT", dna_sequence):
    cuts_list.append(AbcI_match.start()+3)

# This iterates through a given string or list. The cut is at GC[AG][AT]^TG. The cut is at index 4 or character 5.
for AbcII_match in re.finditer(r"GC[AG][AT]TG", dna_sequence):
    cuts_list.append(AbcII_match.start()+4)

# This takes the length of the whole sequence to assume that there was no splices.
cuts_list.append(len(dna_sequence))
# print(cuts_list)
sorted_cuts_list = sorted(cuts_list)
print("The spliced lengths are:")
print("\t" + str(sorted_cuts_list))

print("The Fragment Sizes are:")
count = 0
# 1 is used in range rather than 0 because 0 would take the last index and subtract it with the first index rather than the next and previous.
for i in range(1, len(sorted_cuts_list)):
    count += 1
    current_cut_position = sorted_cuts_list[i]
    previous_cut_positon = sorted_cuts_list[i-1]
    fragment_length = current_cut_position - previous_cut_positon
    print("\t" + "Fragment" + "\t" + str(count) +
          "\t" + "is" + "\t" + str(fragment_length))
