# Authored by : yj2221
# Co-authored by : -
# Link : http://boj.kr/22ca7154f6ec4ff0b8749054c40fa809

import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

T = int(input())

def dijk(start, dependency):
    pq = [[0,start]]
    result = [99999999 for _ in range(n+1)]
    result[start] = 0
    while pq:
        cur_time, cur = heapq.heappop(pq)
        for _next, next_time in dependency[cur].items():
            time = cur_time + next_time
            if result[_next]>time:
                result[_next] = time
                heapq.heappush(pq,[time, _next])
    return result

for _ in range(T):
    n, d, c = map(int,input().split())
    dependency = {i:{} for i in range(1,n+1)}
    for _ in range(d):
        a, b, s = map(int,input().split())
        dependency[b][a] = s
        
    result = dijk(c,dependency)
    cnt = 0
    _max = 0
    for value in result:
        if value==99999999:
            continue
        cnt+=1
        _max = max(_max, value)
    print(cnt, _max)