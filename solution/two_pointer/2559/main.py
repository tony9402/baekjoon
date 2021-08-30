# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/1d6b566a715d4126b3cd42cc39521ac0

import sys

def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
arr = list(map(int, input().split()))
total = 0
MAX = -1e9
s, e = 0, K-1
if K == 1:
    print(max(arr))
else:
    total = sum(arr[:K])
    while True:
        MAX = max(MAX, total)
        total -= arr[s]
        s += 1
        e += 1
        if e == N:
            break
        total += arr[e]
    print(MAX)