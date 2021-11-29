# Authored by : tony9402
# Co-authored by : -
# Link : http://boj.kr/9908832547364dfd87342eb0a2a873ce
import sys

def input():
    return sys.stdin.readline().rstrip()

s = input()
N = len(s)

index = [ -1 for _ in range(N) ]
stack = []
current_index = 0

# 올바른 괄호만 주어진다. 각 괄호 쌍에 차례대로 index를 붙여주고 기록하자.
for idx, ch in enumerate(s):
    if ch == '(':
        stack.append(current_index)
        index[idx] = current_index
        current_index += 1
    elif ch == ')':
        index[idx] = stack.pop()

# 각 괄호에 번호를 기록해놨다. 이제 재귀를 돌아 괄호쌍을 뽑자.
answer = [] # 가능한 모든 것을 저장 후 정렬 후 출력하기 위해 사용

# current_index ==> bracket count
choose = [ 0 for _ in range(current_index) ]

# cnt -> bracket index 번호
def func(cnt): 
    if cnt == current_index:
        erase_bracket_count = sum(choose)
        if erase_bracket_count == 0:
            return

        string = ""
        for idx, ch in enumerate(s):
            # index[idx] == -1 인 경우 (괄호가 아니므로 추가)
            # 만약 -1이면 뒤에 조건문이 실행 안됨
            if index[idx] == -1 or choose[index[idx]] == 0:
                string += ch

        answer.append(string)
        return

    choose[cnt] = 1 # 해당 괄호쌍을 지운 경우
    func(cnt + 1)
    choose[cnt] = 0 # 해당 괄호쌍을 지우지 않은 경우
    func(cnt + 1)

# Run 
func(0)
# 정답 중에 중복이 있을 수 있기 때문에 중복 제거
answer = sorted(set(answer))
print('\n'.join(answer))
