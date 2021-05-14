# Authored by : chj3748
# Co-authored by : -
# http://boj.kr/8f470025f1ae478d8e24a0ff85d0d873
import sys

def input():
    return sys.stdin.readline().rstrip()

# 상하반전
def fun1(arr):
    r_num = len(arr)
    c_num = len(arr[0])
    temp = [arr[-(row + 1)] for row in range(r_num)]
    return temp

# 좌우반전
def fun2(arr):
    arr_N = len(arr)
    arr_M = len(arr[0])
    temp = [arr[row][::-1] for row in range(arr_N)]
    return temp

# 오른쪽90, 시계방향 90
def fun3(arr):
    arr_N = len(arr)
    arr_M = len(arr[0])
    temp = [[arr[-(col + 1)][row] for col in range(arr_N)] for row in range(arr_M)]
    return temp

# 왼쪽 90, 반시계 90
def fun4(arr):
    arr_N = len(arr)
    arr_M = len(arr[0])
    temp = [[arr[col][-(row + 1)] for col in range(arr_N)] for row in range(arr_M)]
    return temp

# 서브 그룹 오른쪽90 회전
def fun5(arr):
    r_num = len(arr)
    c_num = len(arr[0])
    h_rn = r_num // 2
    h_cn = c_num // 2
    temp = [[0] * c_num for _ in range(r_num)]
    for row in range(r_num):
        for col in range(c_num):
            if row < h_rn and col < h_cn:
                temp[row][col] = arr[row + h_rn][col]
            elif row < h_rn and col >= h_cn:
                temp[row][col] = arr[row][col - h_cn]
            elif row >= h_rn and col < h_cn:
                temp[row][col] = arr[row][col + h_cn]
            elif row >= h_rn and col >= h_cn:
                temp[row][col] = arr[row - h_rn][col]
    return temp

# 서브 그룹 왼쪽90 회전
def fun6(arr):
    r_num = len(arr)
    c_num = len(arr[0])
    h_rn = r_num // 2
    h_cn = c_num // 2
    temp = [[0] * c_num for _ in range(r_num)]
    for row in range(r_num):
        for col in range(c_num):
            if row < h_rn and col < h_cn:
                temp[row][col] = arr[row][col + h_cn]
            elif row < h_rn and col >= h_cn:
                temp[row][col] = arr[row + h_rn][col]
            elif row >= h_rn and col < h_cn:
                temp[row][col] = arr[row - h_rn][col]
            elif row >= h_rn and col >= h_cn:
                temp[row][col] = arr[row][col - h_cn]
    return temp


N, M, R = map(int, input().split())
array = [input().split() for _ in range(N)]
for operator in input().split():
    array = locals()['fun' + operator](array)

for row in array:
    print(' '.join(row))