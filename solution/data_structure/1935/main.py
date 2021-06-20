# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/db333837b5af4d84a2a5ba1dc83d2086
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = input()
oper = '+-*/'
dic = {}
stack = []
num = deque()

for i in range(N):
    num.append(int(input()))

for i in arr:
    if i not in dic and i not in oper:
        dic[i] = num.popleft()

for i in arr:
    if i not in oper:
        stack.append(dic[i])
    else:
        if i == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(b+a)
        elif i == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif i == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(b*a)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(b/a)

print(f"{stack[0]:.2f}")
