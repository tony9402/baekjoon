# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/7800ff5a4f2d4764851c251826604eaa

import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
if N < 5:
    if N % 2 != 0:
        print(-1)
    else:
        print(N // 2)
else:
    ct, N = divmod(N, 5)
    if N == 0:
        print(ct)
    else:
        if N % 2 == 0:
            ct += N // 2
            print(ct)
        else:
            ct -= 1
            N += 5
            ct += N // 2
            print(ct)