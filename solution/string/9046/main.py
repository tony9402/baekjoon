# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/ecd357e546d24b059db0160435e99364
import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
for i in range(N):
    a = input()
    total = {}
    for j in a:
        if j == ' ':
            continue
        if j not in total:
            total[j] = 1
        else:
            total[j] += 1
    new_total = list(total.items())
    if len(new_total) == 1:
        print(new_total[0][0])
    else:
        new_total.sort(key = lambda x : -x[1])
        if new_total[0][1] == new_total[1][1]:
            print('?')
        else:
            print(new_total[0][0])