d = int(input())


for i in range(d):
   if i == 0 or i == d - 1:
           print("* " * (d - 1) + "*")
   else:
       print("*" + "  " * (d - 2) + " *")