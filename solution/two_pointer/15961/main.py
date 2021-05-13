# Authored by : kis03160
# Co-authored by : tony9402
# Link : http://boj.kr/a074da0ce3c34775a50d386da92800e4
import sys

def input():
    return sys.stdin.readline().rstrip()

def answer(line, max_seq, coupon):

    count = 0
    for i in range(max_seq):
        food_number = line[i]
        if not eat[food_number]:
            count += 1
        eat[food_number] += 1

    max_count = count
    for i in range(1, n):
        if max_count <= count:
            if not eat[coupon]:
                max_count = count + 1
            else:
                max_count = count

        out = i - 1
        eat[line[out]] -= 1
        if not eat[line[out]]:
            count -= 1
            
        in_ = (i + max_seq - 1) % n
        if not eat[line[in_]]:
            count += 1
        eat[line[in_]] += 1

    return max_count

n, f_kind, max_seq, coupon = map(int, input().split())
line = [int(input()) for _ in range(n)]
eat = [0 for _ in range(3000001)]
print(answer(line, max_seq, coupon))
