# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/cc59c57fb1534ac4831b7f44f87831be

import sys
def input():
    return sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    oper = str(input())
    n = int(input())
    lst = str(input())[1:-1].split(',')
    if not lst[0].isdigit():
        lst = [] #빈 list가 들어올 경우 따로 처리

    l_p, r_p, front = 0, len(lst), True
    for p in oper:
        if p == 'R': #D operation이 일어날 위치 설정
            front = not front
        else: #D operation 수행
            if front: #앞에서 제거
                l_p += 1
            else: #뒤에서 제거
                r_p -= 1
        if l_p > r_p: #지울 수 없는데 지운 경우
            print('error')
            break
    if l_p <= r_p:
        if front:
            sol = lst[l_p:r_p]
        else:
            sol = list(reversed(lst[l_p:r_p]))
        print('['+','.join(sol)+']') #출력 형식 맞추기