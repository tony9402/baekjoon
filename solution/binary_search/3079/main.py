# Authored by : yj2221
# Co-authored by : -
# Link : http://boj.kr/efcb8c8f772044538717ee1203d7c02d

import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
    
low, high = 0, 1000000000 * m
while low <= high:
    mid = (low + high)//2
    cnt = 0
    for time in arr:
        cnt += mid//time
    if cnt>=m:
        high = mid - 1
    else:
        low = mid + 1

print(low)
