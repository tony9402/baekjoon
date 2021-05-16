# Authored by : chj3748
# Co-authored by : -
# Link : http://boj.kr/35708a61bb1d4149952929e8154ba152
import sys

def input():
    return sys.stdin.readline().rstrip()

def palin(start, end, del_cnt):
    if del_cnt == 2:
        return del_cnt
    while start <= end:
        if string[start] != string[end]:
            a = palin(start + 1, end, del_cnt + 1)
            b = palin(start, end - 1, del_cnt + 1)
            return a if a <= b else b
        start += 1
        end -= 1
    else:
        return del_cnt

for T in range(int(input())):
    string = input()
    print(palin(0, len(string) - 1, 0))
