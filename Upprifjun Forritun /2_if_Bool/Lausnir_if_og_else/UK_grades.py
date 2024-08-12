grade = float(input("What mark did you get?: "))

# Leid 1
if 7 <= grade <= 10:
    print("You got an A")
elif 6 <= grade < 7:
    print("You got a B")
elif 5 <= grade < 6:
    print("You got a C")
elif 4 <= grade < 5:
    print("You got a D")
else:
    print("You got an F")
