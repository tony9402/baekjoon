# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/1649bc736d5e4692b067d78aa43b2edc
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
ans = N
for i in range(N):
    a = input()
    dic = {}
    while True:
        flag = 0
        for j in range(len(a)-1):
            if a[j] == a[j+1]:
                a = a[:j] + a[j+1:]
                flag = 1
                break
        if flag == 0:
            break
    for j in a:
        if j not in dic:
            dic[j] = 1
        else:
            ans -=1
            break
print(ans)