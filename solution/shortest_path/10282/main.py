# Authored by : yj2221
# Co-authored by : tony9402
# Link : http://boj.kr/b4c107ca25f442e8bef9f8486e248741

import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

INF = 99999999

def dijkstra(start, dependency):
    pq = [[0,start]]
    result = [INF for _ in range(n+1)]
    result[start] = 0
    while pq:
        cur_time, cur = heapq.heappop(pq)
        for next_com, next_time in dependency[cur].items():
            time = cur_time + next_time
            if result[next_com] > time:
                result[next_com] = time
                heapq.heappush(pq, [time, next_com])
    return result

for testcase in range(int(input())):
    n, d, c = map(int,input().split())
    dependency = {i:{} for i in range(1,n+1)}
    for _ in range(d):
        a, b, s = map(int,input().split())
        dependency[b][a] = s
        
    result = dijkstra(c, dependency)
    result = [value for value in result if value != INF]
    print(len(result), max(result))
