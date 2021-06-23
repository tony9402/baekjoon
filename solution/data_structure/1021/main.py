# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/71a5091026cf4a1b836dc46c812aeaca
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
queue = deque([i for i in range(1,N+1)])
ans = 0
for i in arr:
    idx = queue.index(i)
    if idx == 0:
        queue.popleft()
    else:
        if idx <= len(queue)//2:
            queue.rotate(-idx)
            queue.popleft()
            ans += idx
        else:
            queue.rotate(len(queue) - idx)
            ans += len(queue) - idx
            queue.popleft()
print(ans)