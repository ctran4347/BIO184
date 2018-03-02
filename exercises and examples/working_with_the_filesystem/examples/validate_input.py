answer = ""
while answer < 1 or answer > 10:
    answer = int(raw_input("enter a number between 1 and 10\n"))
print("final answer is " + str(answer))