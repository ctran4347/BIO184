import os
os.system('clc||clear')

go_terms = open("go_terms.midterm2.txt").read()

import re
list_delimter="\n",
print(re.split(r'\n'+'\g',go_terms))
