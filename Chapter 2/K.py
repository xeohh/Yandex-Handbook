num = int(input())

a = num // 100
b = num % 100 // 10
c = num % 10

max_ = max(a, b, c)
min_ = min(a, b, c)
mid = a + b + c - min_ - max_

if max_ + min_ == mid * 2:
    print(f'YES')
else:
    print(f'NO')