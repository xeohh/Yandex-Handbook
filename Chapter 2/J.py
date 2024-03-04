num = int(input())

num1 = num % 10 + (num % 100 // 10)
num2 = (num % 100 // 10) + (num // 100)

if num1 > num2:
    answer = str(num1) + str(num2)
elif num1 < num2:
    answer = str(num2) + str(num1)
else:
    answer = str(num1) + str(num2)

print(answer)