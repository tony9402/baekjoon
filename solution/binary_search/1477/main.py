# Authored by : yj2221
# Co-authored by : -
# Link : http://boj.kr/b93ed1e8f2a7413fa8fe39483692604f

import sys

def input():
    return sys.stdin.readline().rstrip()

n, m, l = map(int, input().split())
rests = [0] + list(map(int, input().split())) + [l]
rests.sort()

_min = 0
_max = l
answer = _max
while _min <= _max:
    mid = (_min + _max) // 2
    cnt = 0
    for i in range(n+1):
        cnt += (rests[i+1] - rests[i] - 1) // mid 
        
    if cnt<=m:
        answer = mid
        _max = mid-1
    else:
        _min = mid+1
        
print(answer)