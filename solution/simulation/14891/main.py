# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/7ce69b01ff0547dd9aa76e858a7bd215
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

arr = []
ans = 0

for i in range(4):
    arr.append(deque(input()))

K = int(input())

for i in range(K):
    queue = deque()
    a, b = map(int, input().split())
    visited = [0] * 4
    queue.append((a-1,b,arr[a-1][6],arr[a-1][2]))
    visited[a-1] = 1
    arr[a-1].rotate(b)
    while queue:
        n,d,l,r = queue.popleft()
        if n-1 >= 0 and arr[n-1][2] != l and visited[n-1] == 0:
            visited[n-1] = 1
            queue.append((n-1, -d, arr[n-1][6], arr[n-1][2]))
            arr[n-1].rotate(-d)
        if n+1 < 4 and arr[n+1][6] != r and visited[n+1] == 0:
            visited[n+1] = 1
            queue.append((n+1, -d, arr[n+1][6], arr[n+1][2]))
            arr[n+1].rotate(-d)

for i in range(4):
    if arr[i][0] == '1':
        ans += 2 ** i

print(ans)
