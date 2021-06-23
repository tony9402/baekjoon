# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/e59d5d5d486b44ba93000175e5118406
import sys
from math import sqrt

def input():
    return sys.stdin.readline().rstrip()

def GCD(x,y):
    if y == 0:
        return x
    else:
        return GCD(y, x%y)

arr = [0] * 1000003
for i in range(2,int(sqrt(1000003))+1):
    for j in range(i+i, 1000003, i):
        if arr[j] == 0:
            arr[j] = 1
arr[0] = 1
arr[1] = 1
LCM = 1
N = int(input())
A = list(map(int, input().split()))
ans = []
for i in A:
    if not arr[i]:
        ans.append(i)
if not ans:
    print(-1)
else:
    LCM = ans[0]
    for i in range(1,len(ans)):
        LCM = ans[i] * LCM // GCD(ans[i], LCM)
    print(LCM)