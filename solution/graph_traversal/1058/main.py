# Authored by : gkgg123
# Co-authored by : -
# Link : https://www.acmicpc.net/source/share/a369084903d348d2966ab752ccb745ec
import sys
def input():
    return sys.stdin.readline().rstrip()

def dfs(idx):
    global N
    visited = [ True for _ in range(N) ]
    visited[idx] = False
    stack = [ (idx, 0) ]
    total = 0
    while stack:
        curent_x, p_cnt = stack.pop()
        for either_x in range(N):
            if arr[curent_x][either_x] == 'Y':
                if visited[either_x] and p_cnt <= 1:
                    visited[either_x] = False
                    stack.append((either_x, p_cnt+1))
                    total += 1
    return total

N = int(input())
arr = [list(input()) for _ in range(N)]
max_number = 0

for i in range(N):
    cu_cnt = dfs(i)
    max_number = max(max_number,cu_cnt)

print(max_number)
