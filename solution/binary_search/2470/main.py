# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/c487c1f5e7f34df0aaeba6a14fb6b2a5
from bisect import bisect_left
import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
lst_pos, lst_neg = [], []
input_lst = list(map(int, input().split()))
for x in input_lst:
    if x > 0: lst_pos.append(x)
    else: lst_neg.append(x)

lst_pos.sort()
lst_neg.sort()

if not lst_pos: print(*lst_neg[-2:]) # 양수가 없는 경우
elif not lst_neg: print(*lst_pos[:2]) # 음수가 없는 경우
else:
    tmp = 2000000001 #최악 케이스+1
    if len(lst_neg) > 1: # 음수만 가지고 답일 수 있음
        if tmp > abs(sum(lst_neg[-2:])):
            tmp = abs(sum(lst_neg[-2:]))
            sol = lst_neg[-2:]

    if len(lst_pos) > 1: # 양수만 가지고 답일 수 있음
        if tmp > abs(sum(lst_pos[:2])):
            tmp = abs(sum(lst_pos[:2]))
            sol = lst_pos[:2]  

    for num in lst_neg:
        idx = bisect_left(lst_pos, -num)
        if idx == len(lst_pos): idx -= 1 # 마지막 인덱스
        elif idx == 0: pass # 처음 인덱스
        elif abs(num+lst_pos[idx]) > abs(num+lst_pos[idx-1]): # 둘 중 최적 선택
            idx -= 1

        if tmp > abs(num+lst_pos[idx]): # 필요 시 업데이트
            tmp = abs(num+lst_pos[idx])
            sol = sorted([num, lst_pos[idx]])

    print(*sol)
