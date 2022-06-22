# Authored by : pmb0836
# Co-authored by : -
# Link : http://boj.kr/617260d11fd54db7a1b224b92ef4f163
import sys


def input():
    return sys.stdin.readline().rstrip()


a, b = input(), input()
print(1) if a.startswith(b) or a.endswith(b) or len(a.split(b)) > 1 else print(0)
