# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/3ad1b45ad3db4bf7b1bfc5227e1acd12
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

queue = deque()
N = int(input())
for i in range(1,N+1):
    queue.append(i)

while True:
    a = queue.popleft()
    if not queue:
        print(a)
        break
    b = queue.popleft()
    queue.append(b)