# Authored by : seonjoo0885
# Co-authored by : -
# Link : http://boj.kr/af4a5e429c8b437fa5ec7ffdde4ede55

import sys
def input():
    return sys.stdin.readline().rstrip()
INF = float('inf')

n, k = map(int, input().split())
doll = list(map(int, input().split()))
size, cnt, end, ans = 0, 0, 0, INF  # size: 현재 집합의 크기, cnt: 라이언 수, end: 집합의 끝 포인터, ans: 정답

for start in range(n):  # start: 집합의 시작 포인터
    while cnt < k and end < n:  # end를 뒤로 한 칸씩 이동시키면서 라이언 탐색 진행
        if doll[end] == 1:
            cnt += 1
        size += 1
        end += 1

    if cnt == k and ans > size:  # 라이언이 k개가 되었다면 size를 체크해서 정답 업데이트
        ans = size

    if doll[start] == 1:  # start를 뒤로 한 칸 이동시킬 준비
        cnt -= 1
    size -= 1

print(ans if ans != INF else -1)
