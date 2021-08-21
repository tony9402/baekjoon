# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/c3b5f907db554df093b6d9ea748fed35

import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = []
ans = 0
for i in range(N):
    arr.append(int(input()))
arr.sort(key = lambda x : -x)
for i in range(len(arr)):
    tip = arr[i] - i
    if tip > 0:
        ans += tip
print(ans)