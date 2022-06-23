# Authored by : pmb0836
# Co-authored by : -
# Link : http://boj.kr/94a9f9c8580d4810bfc7e93d94117cb4
import sys


def input():
    return sys.stdin.readline().rstrip()


s = input()
stack = []
answer = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        if s[i - 1] == '(':  # 레이저
            stack.pop()
            answer += len(stack)
        else:  # 쇠 막대기 끝
            stack.pop()
            answer += 1

print(answer)
