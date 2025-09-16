word = "APPLE"

letter = input("guess a letter in the secret word: ")

if letter in word:
    print(f"there is a {letter}")
else:
    print(f"there is no {letter}")

#if letter not in word:
#    print(f"there is a {letter}")
#else:
#   print(f"there is no {letter}")