import os
import re
import sys
#----------------------------------------------------------------------
# Clears screen
def clear():
    return os.system("clear")
clear()
#----------------------------------------------------------------------
# Creating dictionary
go_term_dictionary = {}
for go_terms in open(sys.argv[2]):
    if go_terms.startswith("g_"):
        go_term_and_description = go_terms.strip("\n").split("\t")
        term = go_term_and_description[0]
        description = go_term_and_description[1]
        go_term_dictionary[term] = description
# ---------------------------------------------------------------------
#Gene Dictionary
genecode = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
    'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W'}
# TAG,TAA, and TAG are stop codons
# ---------------------------------------------------------------------
# Translates Genes
def translation(sequence):
    protein = ""
    last_codon = len(sequence) - 2
    # Iterates starting at 0 and increases by 3 indexes each time
    for start_position in range(0, last_codon, 3):
        current_codon = sequence[start_position:start_position + 3]
        amino_acid = genecode.get(current_codon, "X")
        protein += amino_acid
    return protein
#-----------------------------------------------------------------------
# Iterates through transcript file and does magic
transcript_terms_list = []
go_terms_transcripts_list = []
max_orf_length_list = []
translated_sequence_list = []
for lines in open(sys.argv[1]):
    if lines.startswith(">"):
        transcripts_input_splitted = re.split("\t|\n", lines)
        transcript_terms_list.append(transcripts_input_splitted[0])
        go_terms_transcripts_list.append(transcripts_input_splitted[1])
    else:
        sequences_input = lines.strip()
        sequence_split = translation(sequences_input).split("*")
        max_orf_length_list.append(len(max(sequence_split, key=len)))
        translated_sequence_list.append(translation(sequences_input))
#-------------------------------------------------------------------------
# Iterates through sorted tuple based on length of max_orf
for transcripts, go, max_orf, translated_sequence in sorted(zip(transcript_terms_list, go_terms_transcripts_list, max_orf_length_list, translated_sequence_list), key=lambda x: x[2]):
    print(f"{transcripts}\tGO:{go_term_dictionary.get(go)}\tMAX:ORF:{str(max_orf)} aa\n{translated_sequence}")
#-------------------------------------------------------------------------
# python3 Midterm_Project_2_improved.py transcripts.midterm2.fasta go_terms.midterm2.txt
