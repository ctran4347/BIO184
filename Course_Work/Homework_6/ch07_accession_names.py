accessions = ['xkn59438', 'yhdck2', 'eihd39d9',
              'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']
import os,re
def clear():
    return os.system("clear")
clear()
output1=open("ch07_accessions_names.FASTA","w")

output1.write(">contain the number 5")

for names in accessions:
# r (raw) results to any special characters being ignored such as \t or \n
    if re.search(r"5", names):
        output1.write("\n" + names)

output1.write("\n" + ">contain the letter d or e")
for names in accessions:
    if re.search(r"d|e", names):  # the special character | allows us to do a kind of OR statement where it would include names that include d OR e
       output1.write("\n" + names)

output1.write("\n" + ">contain the letters d and e in that order")
for names in accessions:  # .* is basically and
    # the special character (.) or period or dot would match with any character in the input with one character in between. * will match any repetitions so essentially. d*e will match e,de,dee.
    if re.search(r"d.*e", names):
        output1.write("\n" + names)

output1.write("\n" + ">contain the letters d and e in that order with a single letter between them")
for names in accessions:
    # this would only match the characters in that order with a single character between them
    if re.search(r"d.e", names):
        output1.write("\n" + names)

output1.write("\n" + ">contains both the letter d and e in any order")
for names in accessions:
    # This is basically the same as re.search(r"d.*e") or re.search(r"e.*d")
    if re.search(r"d.*e|e.*d", names):
        output1.write("\n" + names)

output1.write("\n" + ">start with x or y")
for names in accessions:
    if re.search(r"^(x|y)", names):  # the paranthesis are necessary to utilize both characters
       output1.write("\n" + names)

output1.write("\n" + ">start with x or y and end with e")
for names in accessions:
    # $ is a special character that will search for the end of said character. GGG$ would watch AAAGGG.
    if re.search(r"^(x|y).*e$", names):
        output1.write("\n" + names)

output1.write("\n" + "> contains three or more digits in a row")
for names in accessions:
    # [] is a character group and {} is a quantifer
    if re.search(r"[123456789]{3,100000000}", names):
        output1.write("\n" + names)

output1.write(">end with d followed by either a,r,or p")
for names in accessions:
    if re.search(r"d[arp]$", names):
        output1.write("\n" + names)
