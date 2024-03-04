petya = int(input())
vasya = int(input())
tolya = int(input())

max_ = max(petya, vasya, tolya)
min_ = min(petya, vasya, tolya)
other = petya + vasya + tolya - max_ - min_

if max_ == petya:
    first = 'Петя'
elif max_ == vasya:
    first = 'Вася'
else:
    first = 'Толя'

if other == petya:
    second = 'Петя'
elif other == vasya:
    second = 'Вася'
else:
    second = 'Толя'

if min_ == petya:
    third = 'Петя'
elif min_ == vasya:
    third = 'Вася'
else:
    third = 'Толя'

one = 'I'
two = 'II'
three = 'III'

print(f'{first: ^24}')
print(f'{second: ^8}')
print(f'{third: >22}')
print(f'{two: ^8}{one: ^8}{three: >5}')