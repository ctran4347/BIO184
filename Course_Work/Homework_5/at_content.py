#Single gene in order of: Species name, sequence, gene name, expression level


data=open("data.csv")
def at_content(dna):
    dna_length=len(dna) # determines length of dna sequence or a string
    a_count=dna.upper().count("A") #counts the number of A's in the strng
    t_count=dna.upper().count("T") #counts the number of T's in the string
    a_t_content=((a_count + t_count)/dna_length) # determines the AT content in said DNA length
    return a_t_content
for gene_names in data:
    order=gene_names.replace("\n","").split(",") # Removes white space for each line and splits commas into a list
    species_name=order[0]   
    sequence=order[1]
    gene_name=order[2]
    expression_level=order[3]
    expression_level_integer=int(expression_level)
    if at_content(sequence) < 0.5 and expression_level_integer > 200:
        print(gene_name)
    else:
        pass


      