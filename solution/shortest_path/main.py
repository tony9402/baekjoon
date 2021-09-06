# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/6d0558a4848c49098f08a06f655cd86c

from heapq import heappush, heappop
import sys
def input():
    return sys.stdin.readline().rstrip()

def dijkstra(road, start):
    dp = [10000000]*(n+1)
    dp[start] = 0
    heap = []
    heappush(heap, [0, start])

    while heap:
        time, cur = heappop(heap)

        if time > dp[cur]: #기존 경로 사용
            continue

        for t, nei in road[cur]:
            new_t = t + time
            if new_t < dp[nei]:
                dp[nei] = new_t
                heappush(heap, [new_t, nei])
    return dp

n, m, k = map(int, input().split())
road = [[] for _ in range(n+1)]
road_r = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, t = map(int, input().split())
    road[x].append([t, y])
    road_r[y].append([t, x])
    
dp = dijkstra(road, k)
dp_r = dijkstra(road_r, k)

print(max([dp[i]+dp_r[i] for i in range(1, n+1)]))