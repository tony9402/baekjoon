# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/2b640a2f6eb74e08aae6e351cfcbf537

import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = [i for i in range(1, N+1)]
s, e = 0, 0
ans = 0
total = 0
while True:
    if total < N:
        total += arr[e]
        e += 1
    elif e == len(arr):
        break
    elif total >= N:
        if total == N:
            ans += 1
        total -= arr[s]
        s += 1
print(ans+1)