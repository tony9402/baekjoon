# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/3ba9e83879cc4489a5db43c977f87f45

import sys

def input():
    return sys.stdin.readline().rstrip()

def DFS(x):
    global MAX
    if len(arr) == 2:
        MAX = max(MAX, x)
        return
    for i in range(1, len(arr)-1):
        save = arr[i]
        arr.pop(i)
        DFS(x + arr[i-1] * arr[i])
        arr.insert(i, save)

N = int(input())
MAX = 0
arr = list(map(int, input().split()))
DFS(0)
print(MAX)
