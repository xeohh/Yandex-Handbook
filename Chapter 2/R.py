a = int(input())
b = int(input())
c = int(input())

max_ = max(a, b, c)
min_ = min(a, b, c)
mid = a + b + c - max_ - min_

mul = min_ ** 2 + mid ** 2

if mul == max_ ** 2:
    print('100%')
elif mul > max_ ** 2:
    print('крайне мала')
else:
    print('велика')