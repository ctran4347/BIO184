my_file=open("input.txt")
output=open("trimmed.txt","w")
for each_line in my_file:
    length=len(each_line)
    trimmed=each_line[13:length]
    output.write(trimmed)
print("The length of the sequence is " + str(length))
    
