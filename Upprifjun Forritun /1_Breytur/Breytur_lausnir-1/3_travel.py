meters = float(input("How many meters did you travel: "))
minutes = int(input("How long did it take in minutes?: "))

# meters -> km
kilometers = meters/1000

# minutes -> klst
klst = minutes/60

# km/klst
km_per_klst = kilometers/klst
# Finna 'ut leid til að prenta bara 2 aukastafi
km_per_klst = round(km_per_klst, 2)

print(f"You were traveling {km_per_klst}km/h")