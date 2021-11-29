# Authored by : yj2221
# Co-authored by : tony9402
# Link : http://boj.kr/3fe7ddd4b0c2437882109089a41a0349

import sys

def input():
    return sys.stdin.readline().rstrip()

n, m, l = map(int, input().split())
rests = [0] + list(map(int, input().split())) + [l]
rests.sort()

low = 1
high = l
answer = high
while low <= high:
    mid = (low + high) // 2
    
    cnt = 0
    for i in range(n+1):
        cnt += (rests[i+1] - rests[i] - 1) // mid 
        
    if cnt<=m:
        answer = mid
        high = mid - 1
    else:
        low = mid + 1
        
print(answer)
