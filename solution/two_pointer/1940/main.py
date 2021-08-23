# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/901436e12d914d5e9effcd67494bbb44

import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
s, e = 0, len(arr) - 1
while s < e:
    if arr[s] + arr[e] > M:
        e -= 1
    elif arr[s] + arr[e] < M:
        s += 1
    else:
        s += 1
        e -= 1
        ans += 1
print(ans)