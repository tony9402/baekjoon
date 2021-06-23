# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/b60f3d6809514134b0740ee31eeb763a
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
ans = 0
if N == 0:
    print(ans)
else:
    queue = deque(list(map(int, input().split())))
    while True:
        weight = 0
        while weight + queue[0] <= M:
            weight += queue.popleft()
            if not queue:
                break
        ans += 1
        if not queue:
            break
    print(ans)