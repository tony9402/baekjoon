# Authored by : seonjoo0885
# Co-authored by : -
# Link : http://boj.kr/f51e261bb49e48abb9875d763a5e79f2

import sys
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
lst = list(map(int, input().split()))

dic = defaultdict(int)
size, ans, end = 0, 0, 0

for start in range(n):
    while end < n and dic[lst[end]] < k:  # 현재 수열에 현재 수가 k개 미만 담겨있다면 수열에 담아주고, end를 한 칸씩 뒤로 이동시키며 계속 탐색
        dic[lst[end]] += 1
        size += 1
        end += 1
    if ans < size:  # 더 긴 수열을 발견하면 정답 업데이트
        ans = size
        
    # start를 한 칸 뒤로 이동시켜주기 위해 준비
    size -= 1
    dic[lst[start]] -= 1

print(ans)
