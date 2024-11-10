# Step 1: Ask for the number of players
while True:
    p = int(input(""))
    if p >= 2:
        break  # Ensure there are at least 2 players

# Step 2: Collect contributions from each player
contributions = []
for i in range(p):
    contribution = int(input(""))
    contributions.append(contribution)

# Step 3: Calculate the sum of all contributions
total = sum(contributions)

# Step 4: Determine the winner
remainder = total % p

# Step 5: Output the results
print(f"The sum of all contributions is {total}")
print(f"When {total} is divided by {p}, the remainder is {remainder}")  # Added comma for correct format
print(f"Player {remainder} is the winner!")