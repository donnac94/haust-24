a = int(input("Enter in the one side of the triangle: "))
b = int(input("Enter in the second side of the triangle: "))
c = int(input("Enter in the third side of the triangle: "))

if (( a == b) and (b == c)):
  print("This is an equilateral triangle")
elif (a == b) or (a == c) or (b == c):
  #if any two sides of the triangles are equal 
  print("This is an isoceles triangle")
else:
  print("This is a scalene triangle")
  
    

