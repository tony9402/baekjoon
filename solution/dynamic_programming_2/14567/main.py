# Authored by : yj2221
# Co-authored by : tony9402
# Link : http://boj.kr/563199054385492b8f7e25eca46a2696

from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

learning = {i:[] for i in range(1, n+1)}
indegree = [0] * (n+1)
dp = [1] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    learning[a].append(b)
    indegree[b] += 1
    
q = deque()
for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    for nxt in learning[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)
            dp[nxt] = max(dp[nxt], dp[cur]+1)

print(' '.join(map(str,dp[1:])))
