x = int(input("Enter a number: "))

def square(x):
    return x**2 # square the number

def root(x): 
  return x**0.5 # square root the number

def even_or_odd(x): # check if the number is even or odd
    if x % 2 == 0: #  if the number is divisible by 2
        return "Even" 
    else:
        return "Odd"


print(f"The square of {x} is {square(x)}") 
print(f"The square root of {x} is {root(x)}")
print(f"The number {x} is {even_or_odd(x)}")