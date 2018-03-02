from __future__ import division
def get_at_content(dna): 
    length = len(dna) 
    a_count = dna.count('A') 
    t_count = dna.count('T') 
    at_content = (a_count + t_count) / length 
    return at_content 

print("AT content is " + str(get_at_content("ATGACTGGACCA")))
