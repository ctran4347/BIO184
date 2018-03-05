from __future__ import division

def is_at_rich(dna):
	length = len(dna)
	a_count = dna.upper().count('A')
	t_count = dna.upper().count('T')
	at_content = (a_count + t_count) / length
	if at_content > 0.65:
		return True
	else:
		return False
