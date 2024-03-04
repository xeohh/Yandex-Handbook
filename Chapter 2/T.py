flag = False
one = input()
if 'зайка' in one:
    flag = True
    ans = one + ' ' + str(len(one))
    prim = one

two = input()
if 'зайка' in two:
    if flag:
        if prim > two:
            ans = two + ' ' + str(len(two))
            prim = two
    else:
        flag = True
        ans = two + ' ' + str(len(two))
        prim = two

three = input()
if 'зайка' in three:
    if flag:
        if prim > three:
            ans = three + ' ' + str(len(three))
    else:
        ans = three + ' ' + str(len(three))


print(ans)