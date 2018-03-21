accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']
import re

for names in accessions:
    if re.search(r"5",names): #r (raw) results to any special characters being ignored such as \t or \n
        print("Accessions that contain number 5 is", names)


for names in accessions:
    if re.search(r"d|e",names): #the special character | allows us to do a kind of OR statement where it would include names that include d OR e
        print("Accesions that contain letter d OR e is", names)

for names in accessions: # .* is basically and
    if re.search(r"d.*e",names): # the special character (.) or period or dot would match with any character in the input with one character in between. * will match any repetitions so essentially. d*e will match e,de,dee.  
        print("Accessions that contain the letters d and e in that order (Anything in between is possible)",names)

for names in accessions:
    if re.search(r"d.e",names): # this would only match the characters in that order with a single character between them
        print("Accessions that contain the letters d and e in that order with a single letter between them", names)
        

for names in accessions:
    if re.search(r"d.*e|e.*d",names): # This is basically the same as re.search(r"d.*e") or re.search(r"e.*d")
        print("Accessions that contains both letter d and e in any order",names)


for names in accessions:
    if re.search(r"^(x|y)",names): # the paranthesis are necessary to utilize both characters
        print("Accessions tht start with x or y is", names)


for names in accessions:
    if re.search(r"^(x|y).*e$",names): # $ is a special character that will search for the end of said character. GGG$ would watch AAAGGG.
        print("Accessions that start with x or y and ends with e",names)
    
for names in accessions:
    if re.search(r"[123456789]{3,100000000}",names): #[] is a character group and {} is a quantifer
        print("Accessions that contain three or more numbers in a row",names)
    
for names in accessions:
    if re.search(r"d[arp]$",names):
        print("Accessions that end with d followed by either a, r or p", names)