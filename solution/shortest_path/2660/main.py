# Authored by : seonjoo0885
# Co-authored by : -
# Link : http://boj.kr/b551078ad4194be08eb8a4bd0e7e7511

import sys, heapq
def input():
    return sys.stdin.readline().rstrip()
INF = float('inf')

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF for _ in range(n)]
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    distance[start] = 0
    return distance

n = int(input())
graph = [[] for _ in range(n)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a-1].append((b-1, 1))
    graph[b-1].append((a-1, 1))

minVal = INF
minPerson = []

for i in range(n):
    score = max(dijkstra(i))
    if minVal > score:
        minVal = score
        minPerson = [i+1]
    elif minVal == score:
        minPerson.append(i+1)

print(minVal, len(minPerson))
print(*minPerson)
