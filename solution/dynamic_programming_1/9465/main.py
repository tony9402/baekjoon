# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/39643867e537451a9ae49e16ec4f2f3f

import sys
def input():
    return sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n = int(input())
    lst = [list(map(int, input().split())) for i in range(2)]
    # 새로 dp 행렬 만들 필요 없이 스티커 값이 저장된 lst 배열에서 dp 수행

    if n > 1:
        # 경우의 수 오직 1개
        lst[0][1] += lst[1][0]
        lst[1][1] += lst[0][0]

    if n > 2:
        for i in range(2, n):
            #대각선에 있는 스티커를 고를 지, 거기서 한 칸 더 떨어져 있는 스티커를 고를 지 선택
            lst[0][i] += max(lst[1][i-1], lst[1][i-2])
            lst[1][i] += max(lst[0][i-1], lst[0][i-2])

    print(max(lst[0][-1], lst[1][-1]))
