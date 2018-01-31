sequence_header_ABC123="ATCGTACGATCGATCGATCGCTAGACGTATCG"
sequence_header_DEF456="actgatcgacgatcgatcgatcacgact"
sequence_header_HIJ789="ACTGAC-ACTGT--ACTGTA----CATGTG"
new_sequence_header_DEF456=sequence_header_DEF456.upper()
new_sequence_header_HIJ789=sequence_header_HIJ789.replace("-","")
sequence_header_ABC123_file=open("ABC123.fasta","w")
sequence_header_ABC123_file.write(">Sequence_ABC123\n" + sequence_header_ABC123)
sequence_header_DEF456_file=open("DEF456.fasta","w")
sequence_header_DEF456_file.write(">Sequence_DEF456\n" + new_sequence_header_DEF456)
sequence_header_HIJ789_file=open("HIJ789.fasta","w")
sequence_header_HIJ789_file.write(">Sequence_HIJ789\n" + new_sequence_header_HIJ789)