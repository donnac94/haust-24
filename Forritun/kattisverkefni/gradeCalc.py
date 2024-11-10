# This program  takes in a grade and returns the letter grade that corresponds to it.

grade = int(input("Enter your grade: "))

if grade <= 90:
  print("A")
elif 80 <= grade < 90:
  print("B")
elif 70 <= grade < 80:
  print("C")
elif 60 <= grade < 70:
  print("D")
else: 
  print("F")
  
