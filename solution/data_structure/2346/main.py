# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/71af42c3664749e48f8f0272c3c04fd2
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
queue = deque(list(map(int, input().split())))
queue2 = deque([i for i in range(1,N+1)])
while queue:
    q = queue[0]
    if q > 0:
        queue.popleft()
        queue.rotate(-q+1)
        print(queue2.popleft())
        queue2.rotate(-q+1)
    else:
        queue.popleft()
        queue.rotate(-q)
        print(queue2.popleft())
        queue2.rotate(-q)