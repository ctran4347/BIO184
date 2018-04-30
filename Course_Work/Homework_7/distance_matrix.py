import os, sys
os.system("cls")
gene_set={}
for metal in open(sys.argv[1]): #Replace with system.argv[2]
    split=metal.strip("\n").split("\t")
    metal_name=split[0] # metal name
    condition=set(split[1].split(",")) # conditions created into set
    gene_set[metal_name]=condition
set_1=gene_set[sys.argv[2]] #first condition set for sys.argv input metal
set_2=gene_set[sys.argv[3]] #second condition set for sys.argv input metal
similarity=len(set_1.intersection(set_2))/len(set_1.union(set_2))
print(similarity)
#python distance_matrix.py heavy_metals.txt arsenic cadmium
