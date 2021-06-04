# Authored by : kis03160
# Co-authored by : tony9402
# Link : http://boj.kr/2cb5e18deb964794bec3e960225ad83e
from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()

def answer(G, r):
    is_giga_find = False
    longest = 0
    body = 0
    visited = [False for _ in range(len(G))]
    q = deque()
    q.append((0, r))
    visited[r] = True

    while q:
        dist, node = q.popleft()

        if dist > longest:
            longest = dist

        # 기가 가지가 아직 안나왔고, 2개 이상 연결되어있을 때
        # or V자
        if not is_giga_find and len(G[node]) > 2 \
            or (node == r and len(G[node]) >= 2):
            is_giga_find = True
            body = dist

        for branch in G[node]:
            if not visited[branch]:
                visited[branch] = True
                q.append((dist + G[node][branch], branch))

    # 기가를 못찾았다 -> 가지가 없다.
    if not is_giga_find:
        body = longest
        longest = body

    # 기둥, 가장 긴 가지 길이(루트~해당가지 길이 - 기둥 길이)
    return body, longest - body

n, r = map(int, input().split())
G = {i: dict() for i in range(n + 1)}
for i in range(n - 1):
    a, b, c = map(int, input().split())
    G[a][b] = c
    G[b][a] = c
print(*answer(G, r))
