string = input()
char = input()  

indices = []

for i in range(len(string)):
  if string[i] == char:
    indices.append(i)

for index in indices:
    print(index)