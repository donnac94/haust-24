rating = int(input()) 

if 2700 <= rating:
    print("Super grandmaster")
elif 2500 <= rating <= 2699:
    print("Grandmaster")
elif 2400 <= rating <= 2500:
    print("International Grandmaster")
elif 999 <= rating < 2400:
    print("Amateur")
else: print("Invalid")