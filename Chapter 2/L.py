a = int(input())
b = int(input())
c = int(input())

max_ = max(a, b, c)
other = a + b + c - max_

if max_ < other:
    print(f'YES')
else:
    print(f'NO')