# // Authored by : chj3748
# // Co-authored by : -
# // Link : https://www.acmicpc.net/source/29179486
import sys


def input():
    return sys.stdin.readline().rstrip()


odd_num = -1
even_num = -1
for number in map(int, input().split()):
    if number % 2:
        if odd_num == -1:
            odd_num = number
        else:
            odd_num *= number
    else:
        if even_num == -1:
            even_num = number
        else:
            even_num *= number
if odd_num != -1:
    print(odd_num)
else:
    print(even_num)
