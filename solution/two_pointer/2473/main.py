# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/4d3bf96075df4b31b9a95038e6c649e6

import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
lst = sorted(list(map(int, input().split()))) # 정렬 필요

res = 4000000000 # INF 대용
sol_candi = []

for i in range(n-2):
    refer = lst[i] # 레퍼런스 값 하나를 잡아놓고
    l_p = i+1 # 레퍼런스 값을 제외한 양 끝에서 투 포인터 이동
    r_p = n-1 # 현재 i 이전에 본 레퍼런스 값은 더 이상 필요 없음!
    while l_p < r_p: # 두 포인터가 만나기 전까지
        cur_sum = refer + lst[l_p] + lst[r_p] # 레퍼런스 값 + 두 포인터가 가리키는 값의 합
        if abs(cur_sum) <= abs(res): # 절댓값이 0에 가까운 것이 목표
            sol_candi = [refer, lst[l_p], lst[r_p]] # 정답 후보군 update
            res = refer + lst[l_p] + lst[r_p]
        #현재 값이 정답이 아니라면 포인터 이동
        if cur_sum < 0:
            l_p += 1
        elif cur_sum > 0:
            r_p -= 1
        else:
            print(*sol_candi) # 정확히 0이 되는 조합을 찾았으면 더 볼 필요 없이
            sys.exit()        # 바로 출력하고 프로그램 종료

print(*sol_candi)
