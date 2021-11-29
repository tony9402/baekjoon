# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/6d0558a4848c49098f08a06f655cd86c

from heapq import heappush, heappop
import sys
def input():
    return sys.stdin.readline().rstrip()

INF = 10000000
def dijkstra(road, start):
    dp = [INF]*(n+1)
    dp[start] = 0
    heap = []
    heappush(heap, [0, start])

    while heap:
        cur_time, cur = heappop(heap)

        if cur_time > dp[cur]: #기존 경로 사용
            continue

        for t, nxt in road[cur]:
            new_time = t + cur_time
            if new_time < dp[nxt]:
                dp[nxt] = new_time
                heappush(heap, [new_time, nxt])
    return dp

n, m, k = map(int, input().split())
road = [[] for _ in range(n+1)]
road_rev = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, t = map(int, input().split())
    road[x].append([t, y])
    road_rev[y].append([t, x])
    
dp = dijkstra(road, k)
dp_rev = dijkstra(road_rev, k)

print(max([dp[i]+dp_rev[i] for i in range(1, n+1)]))
