# Authored by : seonjoo0885
# Co-authored by : -
# Link : http://boj.kr/a2477b2f98024ea684ac88780eb58af4

import sys
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]

eat = defaultdict(int)
maximum = 0
end = k - 1

for start in range(n):
    # 처음 시작할 때 k개 먹어주고, 처음이 아니라면 끝쪽 1개 먹어줌
    if start == 0:
        for i in range(k):
            eat[sushi[i % n]] += 1
    else:
        eat[sushi[end % n]] += 1

    # 먹은 k개 중 쿠폰넘버 초밥이 있었는지에 따라 최댓값 갱신
    if c in eat:
        maximum = max(maximum, len(eat))
    else:
        maximum = max(maximum, len(eat) + 1)

    # 뒤로 한 칸 이동할 준비
    eat[sushi[start]] -= 1
    if eat[sushi[start]] == 0:
        eat.pop(sushi[start])
    end += 1

print(maximum)
