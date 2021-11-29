# Authored by : yj2221
# Co-authored by : -
# Link : http://boj.kr/480b70b04e3b4f5c8dd567bf3bde859c

import heapq
import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = {i:{} for i in range(1, n+1)}
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a][b] = min(graph[a][b], t)
    graph[b][a] = min(graph[b][a], t)

INF = 999999
def dijkstra(start):
    dist_result = [INF for _ in range(n+1)]
    dist_result[start] = 0
    index_result = [None] * (n+1)
    visit = [False] * (n+1)
    visit[start] = True
    pq = [(0, start, [])]
    while pq:
        cur_dist, cur, path = heapq.heappop(pq)
        for next_node, next_dist in graph[cur].items():
            dist = next_dist + cur_dist
            if visit[next_node]: continue
            if dist_result[next_node] <= dist: continue
            dist_result[next_node] = dist
            index_result[next_node] = path + [next_node]
            heapq.heappush(pq, (dist, next_node, index_result[next_node]))
    return index_result
            
for start in range(1, n+1):
    result = dijkstra(start)
    answer = ''
    for i in range(0, n):
        if start==i:
            answer+='-'
        else:
            answer+=str(result[i+1][0])
        answer+=' '
    print(answer[:-1])
