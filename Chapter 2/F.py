year = int(input())
answer = 'NO'

if year % 4 == 0:
    answer = 'YES'
if year % 100 == 0 and year % 400 != 0:
    answer = 'NO'

print(f'{answer}')
