# Authored by : yj2221
# Co-authored by : -
# Link : http://boj.kr/d763c3b0bf67448d841b258e0e12c63e

from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

learning = {i:[] for i in range(1, n+1)}
indegree = [0] * (n+1)
dp = [9999999] * (n+1)
visit = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    learning[a].append(b)
    indegree[b]+=1
    
q = deque()
for i, degree in enumerate(indegree):
    if i == 0: continue
    if degree != 0: continue
    q.append(i)
    dp[i] = 1
    visit[i] = True

while q:
    cur = q.popleft()
    for _next in learning[cur]:
        if visit[_next]: continue
        indegree[_next]-=1
        if indegree[_next] == 0:
            q.append(_next)
            visit[_next] = True
            dp[_next] = min(dp[_next], dp[cur]+1)
        
print(' '.join(map(str,dp[1:])))
