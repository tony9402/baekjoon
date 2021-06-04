# Authored by : gkgg123
# Co-authored by : -
# Link : http://boj.kr/ab9a5bb2d14943b3aefaf98f4648a469
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def bfs(N):
    queue = deque()
    for i in range(1, 10):
        queue.append((i, str(i)))
    while queue:
        if len(result) == N + 1:
            break
        cur_num,totol_num = queue.popleft()
        if cur_num != 0:
            for k in range(cur_num):
                next_num = totol_num + str(k)
                queue.append((k,next_num))
                result.append(next_num)

N = int(input())
result = []
for i in range(10):
    result.append(i)
    
if N >=10:
    bfs(N)
    
if len(result) > N:
    print(result[N])
else:
    print(-1)
