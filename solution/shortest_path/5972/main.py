# Authored by : seonjoo0885
# Co-authored by : -
# Link : http://boj.kr/d59ff06546b141918c6b6fa80dfa665a

import sys, heapq
def input():
    return sys.stdin.readline().rstrip()

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [float('inf')] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dijkstra(1)
distance[1] = 0
print(distance[n])
