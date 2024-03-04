one = int(input())
two = int(input())

a = one // 10
b = one % 10
c = two // 10
d = two % 10

max_ = max(a, b, c, d)
min_ = min(a, b, c, d)
other = (a + b + c + d - max_ - min_) % 10

num = max_ * 100 + other * 10 + min_

print(f'{num}')