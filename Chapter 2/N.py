num = int(input())

a = num // 100
b = num % 100 // 10
c = num % 10

max_ = max(a, b, c)
min_ = min(a, b, c)
mid = a + b + c - max_ - min_

num_min = min_ * 10 + mid
num_max = max_ * 10 + mid

if 0 in [max_, min_, mid]:
    num_min = mid * 10 + min_

if num == num // 100 * 100:
    num_min = num_max

print(num_min, num_max)

