# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/7f225e2c0f214a7a9033560ded2a16d4

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def DFS(ans):
    global MIN, MAX
    if not arr:
        MIN = min(MIN, ans)
        MAX = max(MAX, ans)
        return
    for i in range(4):
        if oper[i] > 0:
            oper[i] -= 1
            first = arr[0]
            if i == 0:
                DFS(ans+arr.popleft())
            elif i == 1:
                DFS(ans-arr.popleft())
            elif i == 2:
                DFS(ans*arr.popleft())
            elif i == 3:
                if ans < 0 and arr[0] > 0 or ans > 0 and arr[0] < 0:
                    div = abs(ans) // abs(arr.popleft())
                    DFS(-div)
                else:
                    DFS(ans//arr.popleft())
            arr.appendleft(first)
            oper[i] += 1

N = int(input())
arr = deque(list(map(int, input().split())))
oper = list(map(int, input().split()))
MIN = 1e9+1
MAX = -1e9-1
DFS(arr.popleft())
print(MAX)
print(MIN)