# Authored by : tony9402
# Co-authored by : -
# Link : http://boj.kr/7d0d2bcb568d4c3d86770e520838ef65
import sys

def input():
    return sys.stdin.readline().rstrip()

def change(num, first = False):
    ret = ''
    while num:
        ret += chr(num % 2 + 48)
        num //= 2
    while len(ret) < 3:
        ret += '0'

    idx = 3
    if first:
        while idx > 1 and ret[idx - 1] == '0':
            idx -= 1
    return ret[:idx][::-1]

N = input()
isFirst = True
for i in range(len(N)):
    print(change(int(N[i]), isFirst),end='')
    isFirst = False
