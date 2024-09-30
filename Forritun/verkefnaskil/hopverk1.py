while True:
    input_value = input()
    if input_value == 'q' or input_value == '0':
        break
    
    num = int(input_value)
    divisor_count = 0
    
    for i in range(1, num + 1):
        if num % i == 0:
            divisor_count += 1
    
    if divisor_count >= 10:
        print("yes")
    else:
        print("no")


n = int(input()) 

for i in range(10, min(100, n + 1)):
    digit_sum = 0
    temp = i
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    if digit_sum ** 2 == n:
        print(i)

for i in range(100, min(1000, n + 1)):
    digit_sum = 0
    temp = i
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    if digit_sum ** 3 == n:
        print(i)