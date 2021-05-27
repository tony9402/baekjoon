# Authored by : klm03025
# Co-authored by : -
# Link : http://boj.kr/1306fa8a1c5a4f4cab631f833d92636a
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
_list = []
q = deque([i + 1 for i in range(N)])

while len(q) != 0:
    q.rotate(-K)
    _list.append(q.pop())

print('<' + ', '.join(map(str, _list)) + '>')