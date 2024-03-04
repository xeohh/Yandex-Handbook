petya = 7
vasya = 6

petya -= 3
vasya += 3

petya += 2

n = int(input())
m = int(input())

petya += n
vasya += m

if petya > vasya:
    print(f'Петя')
else:
    print(f'Вася')