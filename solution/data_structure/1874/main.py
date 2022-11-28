# Authored by : nce0130
# Co-authored by : -
# Link : https://www.acmicpc.net/source/52177549

n = int(input())
stk = []
res = []
cnt = 1
tmp = True

for _ in range(n):
    num = int(input())
    while cnt <= num:
        stk.append(cnt)
        res.append('+')
        cnt += 1

    if stk[-1] == num:
        stk.pop()
        res.append('-')
    else:
        tmp = False
        print('NO')
        break

if tmp == True:
    for i in res:
        print(i)