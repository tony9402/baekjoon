# Authored by : seonjoo0885
# Co-authored by : -
# Link : http://boj.kr/ed86288702a24255a80e9a4d4f84b333

import sys
def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0  # 현재 부분수열의 홀수 갯수
start, end = 0, 0  # 현재 부분수열의 시작 포인터, 끝 포인터
size, size_max = 0, 0  # 현재 부분수열의 길이, 가장 긴 부분수열의 길이

for start in range(n):
    while cnt <= k and end < n:  # 홀수 갯수가 k개 이하이면 end를 뒤로 한 칸씩 이동시키면서 계속 탐색
        if lst[end] % 2:
            if cnt == k:
                break
            cnt += 1
        size += 1
        end += 1

    if size_max < size - cnt:  # 더 긴 짝수 연속 부분수열을 발견하면 size_max 업데이트
        size_max = size - cnt

    if lst[start] % 2:  # start를 이동시켜주기 위해 준비
        cnt -= 1
    size -= 1

print(size_max)
