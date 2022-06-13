# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/3797273460bd47949b10ecc1870b5da2

while True:
    sen = input()
    if sen == '.': # 종료조건
        break
    
    stack = []
    braek = True
    
    for char in sen:
        # 여는 괄호는 stack에 추가
        if char == '(': stack.append(char)
        elif char == '[': stack.append(char)
        
        #닫는 괄호인 경우
        elif char == ')':
            if stack and stack[-1] == '(': stack.pop() # 괄호 매칭이 되면 pop
            else: # 매칭이 안되면 no
                braek = False
                break
        elif char == ']':
            if stack and stack[-1] == '[': stack.pop() # 괄호 매칭이 되면 pop
            else: # 매칭이 안되면 no
                braek = False
                break

    if braek and not stack: print('yes')
    # braek이 False거나(매칭 X) stack에 여는 괄호가 남아있으면
    else: print("no")