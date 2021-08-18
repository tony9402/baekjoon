# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/f386e090dfe84518a7329d6f0a77f8c6
import sys

def input():
    return sys.stdin.readline().rstrip()

def DFS():
    if len(arr) == N:
        print(*arr)
        return
    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(i)
            DFS()
            arr.pop()
            visited[i] = 0

N = int(input())
arr = []
visited = [0] * (N+1)
DFS()