# Authored by : yj2221
# Co-authored by : -
# Link : http://boj.kr/efcb8c8f772044538717ee1203d7c02d

import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
    
_min = 0
_max = 1000000000 * m
answer = _max
while _min<=_max:
    mid = (_min + _max)//2
    cnt = 0
    for time in arr:
        cnt += mid//time
    if cnt>=m:
        _max = mid-1
        answer = min(answer, mid)
    else:
        _min = mid+1
print(answer)
