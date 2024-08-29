
from turtle import home


home_score = 0
away_score = 0

home_name = input("Enter the home team's name: ")
away_name = input("Enter the away team's name: ")

while True:
    user_input = input("Which team scored?: ")
    # Check if the user is done with the program
    if user_input == "done":
        break
    # Check which team scored
    if user_input == home_name:
        home_score += 1
    elif user_input == away_name:
        away_score += 1
    else:
        # Else catches all cases where the user did not input the teams' names
        print("That team is not playing, try again")

# Here we are outside of the while loop, lets determine the output
if home_score > away_score:
    print(f"{home_name} won {home_score}-{away_score}")
elif away_score > home_score:
    print(f"{away_name} won {away_score}-{home_score}")
else:
    print(f"It's a draw {home_score}-{away_score}")