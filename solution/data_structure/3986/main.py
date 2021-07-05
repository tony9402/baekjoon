# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/25fcff12eee34fb6a0f0d4023cac4e4d
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
ans = 0
for i in range(N):
    stack = []
    a = input()
    for i in a:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    if not stack:
        ans += 1
print(ans)