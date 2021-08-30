# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/a020564994b8493a92b189861e35636c

import sys
def input():
    return sys.stdin.readline().rstrip()

n, s = map(int, input().split())
lst = list(map(int, input().split()))

l_p, r_p, cur_sum, min_len = 0, 0, 0, 100002
# cur_sum에 저장되는 구간합: sum(lst[l_p:r_p])

while l_p < n:
    if cur_sum >= s: # 현재 구간이 주어진 s보다 크다면
        min_len = min(min_len, r_p-l_p) #현재 구간 길이(r_p-l_p)가 최소라면 업데이트
        cur_sum -= lst[l_p] #왼쪽 포인터를 한 칸 오른쪽으로 옮기고 구간 합 업데이트
        l_p += 1

    elif r_p == n: #오른쪽 끝에 도달했다면?
        break
    
    else:
        cur_sum += lst[r_p] #오른쪽 구간을 움직여서 구간 합 업데이트
        r_p += 1

print(min_len if min_len < 100001 else 0)
