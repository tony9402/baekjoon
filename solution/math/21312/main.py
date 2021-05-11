# // Authored by : chj3748
# // Co-authored by : -
# // Link : http://boj.kr/21536cc8d28a4570aca6c9b48fc41e26

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
