number = int(input()) 

no_7_found_yet = True

temp = number  
while temp > 0:
    last_digit = temp % 10
    if last_digit == 7:
        no_7_found_yet = False
        break  
    temp = temp // 10


if no_7_found_yet:
    print("The number does not contain 7.")
else:
    print("The number contains 7.")