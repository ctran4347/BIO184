my_file=open(r"C:\BIO184\Homework\Homework_2\3_opening_and_closing_files\genomic_dna.txt")
splitting_genomic_dna=my_file.read()
exon_1=splitting_genomic_dna[:62] 
exon_2=splitting_genomic_dna[90:] 
intron_1=splitting_genomic_dna[63:90]
coding_region=(exon_1 + exon_2)
non_coding_region=intron_1
coding_region_file=open("coding_region.txt","w") #open() is meant to open a file but with "w" it will create a new file if it does not exist
noncoding_region_file=open("noncoding_region.txt","w")
coding_region_file.write(coding_region) # write into file the specific string. The file will be saved to the respective workspace
noncoding_region_file.write(non_coding_region) # write specific string into file. The file will be saved to the respective workspace

