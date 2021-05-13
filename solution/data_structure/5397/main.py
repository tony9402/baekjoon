# // Authored by : chj3748
# // Co-authored by : -
# // Link : http://boj.kr/471d69f455a544769c6c2fa7199442d1
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for test in range(T):
    answer_l = deque()
    answer_r = deque()
    for string in input():
        if string == '<':
            if answer_l:
                temp = answer_l.pop()
                answer_r.appendleft(temp)
        elif string == '>':
            if answer_r:
                temp = answer_r.popleft()
                answer_l.append(temp)
        elif string == '-':
            if answer_l:
                answer_l.pop()
        else:
            answer_l.append(string)
    print(''.join(answer_l + answer_r))
