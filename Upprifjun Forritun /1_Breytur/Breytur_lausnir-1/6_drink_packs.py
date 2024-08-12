
size_of_pack = int(input("How big is the drink pack?: "))
num_of_drinks = int(input("How many are you going to buy?: "))

# The amount of packs we need to buy
amount_of_packs = num_of_drinks//size_of_pack

# Amount of drinks you need to buy seperate
seperate_drinks = num_of_drinks%size_of_pack

print(f"You have to buy {amount_of_packs} packs and {seperate_drinks} seperate")