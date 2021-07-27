# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/0d87fc56124b4871af07567902cc63a2
import sys
from itertools import permutations

def input():
    return sys.stdin.readline().rstrip()
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MAX = -1e9-1
MIN = 1e9+1
oper = []
for i in range(len(B)):
    t = B[i]
    if i == 0:
        for j in range(t):
            oper.append('+')
    elif i == 1:
        for j in range(t):
            oper.append('-')
    elif i == 2:
        for j in range(t):
            oper.append('*')
    elif i == 3:
        for j in range(t):
            oper.append('/')
arr = list(permutations(oper))
for i in range(len(arr)):
    ans = A[0]
    for j in range(len(arr[i])):
        if arr[i][j] == '+':
            ans = ans + A[j+1]
        elif arr[i][j] == '-':
            ans = ans - A[j+1]
        elif arr[i][j] == '*':
            ans = ans * A[j+1]
        elif arr[i][j] == '/':
            if ans < 0 and A[j+1] > 0 or ans > 0 and A[j+1] < 0:
                ans = - ans // A[j+1]
                ans = ans * -1
            else:
                ans = ans // A[j+1]
    MAX = max(MAX, ans)
    MIN = min(MIN, ans)
print(MAX)
print(MIN)