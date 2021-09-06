# Authored by : yj2221
# Co-authored by : -
# Link : http://boj.kr/480b70b04e3b4f5c8dd567bf3bde859c

import heapq
import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
dic = {i:{} for i in range(1, n+1)}
for _ in range(m):
    a, b, t = map(int, input().split())
    dic[a][b] = t
    dic[b][a] = t
    
def dijk(start):
    dist_result = [999999 for _ in range(n+1)]
    dist_result[start] = 0
    index_result = [None] * (n+1)
    visit = [False] * (n+1)
    visit[start] = True
    pq = [(0, start,[])]
    while pq:
        cur_dist, cur, path = heapq.heappop(pq)
        for _next, next_dist in dic[cur].items():
            dist = next_dist + cur_dist
            if visit[_next]: continue
            if dist_result[_next]<=dist: continue
            dist_result[_next] = dist
            index_result[_next] = path + [_next]
            heapq.heappush(pq, (dist, _next, index_result[_next]))
    return index_result
            
for start in range(0, n):
    result = dijk(start+1)
    answer = ''
    for i in range(0, n):
        if start==i:
            answer+='-'
        else:
            answer+=str(result[i+1][0])
        answer+=' '
    print(answer[:-1])