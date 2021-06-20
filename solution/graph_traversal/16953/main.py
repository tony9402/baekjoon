# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/e6b9e893d80948c5b739caaf3030e55f
import sys

def input():
    return sys.stdin.readline().rstrip()

def DFS(x,ct):

    if x == B:
        ans.append(ct)
        return

    if x * 10 + 1 <= B:
        DFS(x * 10 + 1,ct+1)

    if x * 2 <= B:
        DFS(x*2,ct+1)

A, B = map(int, input().split())
ans = []
DFS(A,1)

if ans:
    print(ans[0])

else:
    print(-1)