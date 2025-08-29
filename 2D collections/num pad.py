num_pad = ((1, 2, 3),
           (4, 5, 6), 
           (7, 8, 9), 
           ("*", 0, "#"))#this is a 2D tuple  yeah no shit sherlock (the ai made the start)

for row in num_pad:
    for key in row:
        print(key, end=" ")#if im a dumbass and i forget this the end makes it so it doesnt go to a new line after each print
    print()