import sys
n = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split(" ")))
solve_list = []                             # 누적합을 저장하기 위한 리스트

sum = 0

for i in numbers:
    sum += i
    solve_list.append(sum)

testcase = int(sys.stdin.readline())

for i in range(testcase):
    parts = list(map(int, sys.stdin.readline().split()))
    if parts[0] == 1:                       # 처음부터 j 인덱스까지의 누적합
        print(solve_list[parts[1] - 1])
    else:
        print(solve_list[parts[1] - 1] - solve_list[parts[0] - 2])  # i ~ j 인덱스까지의 누적합
