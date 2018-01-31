sequence_header_ABC123="ATCGTACGATCGATCGATCGCTAGACGTATCG"
sequence_header_DEF456="actgatcgacgatcgatcgatcacgact"
sequence_header_HIJ789="ACTGAC-ACTGT--ACTGTA----CATGTG"
new_sequence_header_DEF456=sequence_header_DEF456.upper()
new_sequence_header_HIJ789=sequence_header_HIJ789.replace("-","")
sequence_header_file=open("three.fasta","w")
sequence_header_file.write(">Sequence_ABC123\n" + sequence_header_ABC123 + "\n")
sequence_header_file.write(">Sequence_DEF456\n" + new_sequence_header_DEF456 + "\n")
sequence_header_file.write(">Sequence_HIJ789\n" + new_sequence_header_HIJ789)