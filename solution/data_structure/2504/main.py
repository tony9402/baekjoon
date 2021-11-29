# Authored by : tony9402
# Co-authored by : -
# Link : http://boj.kr/a35de756ecf642b6b2e116f14ffd6093

import sys
def input():
    return sys.stdin.readline().rstrip()

s = input()
stack = []

# Check Bracket
for ch in s:
    if ch == '(':
        stack.append('(')
    elif ch == '[':
        stack.append('[')
    elif ch == ')':
        if stack and stack[-1] == '(':
            stack.pop(-1)
        else:
            print(0)
            exit(0)
    else:
        if stack and stack[-1] == '[':
            stack.pop(-1)
        else:
            print(0)
            exit(0)

if stack:
    print(0)
    exit(0)

# [open bracket] + Integer + Integer => [open bracket] + Integer
# compress (add) Integers
def compress():
    # Integer를 하나로 합쳐야 하니깐 길이가 2 이상이어야 함.
    while len(stack) > 1:
        # 두 개의 값이 무조건 Integer이어야 하므로
        # Integer면 첫번째 원소가 None으로 되어 있음
        a, integer1 = stack[-1]
        b, integer2 = stack[-2]
        if a or b:
            break
        stack.pop()
        stack.pop()
        stack.append((None, integer1 + integer2))

for ch in s:
    # open bracket -> append ( open bracket, ~ )
    if ch == '(':
        stack.append(('(', 2))
    elif ch == '[':
        stack.append(('[', 3))
    elif ch == ')' or ch == ']': # Must Be len(stack) ≥ 1
        last1, last2 = stack.pop()
        # Case 1 : ~~ open bracket
        if last1 != None:
            stack.append((None, last2))
        # Case 2 : ~~ open bracket, Integer,
        else:
            a, b = stack.pop()
            stack.append((None, last2 * b))
        compress()

print(stack[-1][1])
