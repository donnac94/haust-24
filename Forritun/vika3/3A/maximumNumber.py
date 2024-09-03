max_number = 0 

while True:
  num = int(input())
  
  if num < 0:
    break
  
  if num > max_number:
    max_number = num

print(max_number)