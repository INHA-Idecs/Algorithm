'''
올바른 괄호면 true 리턴, 올바르지 않으면 false 리턴하는 solution
'''

def solution(s):
    now = s[0]
    if now != '(': # 시작부터 틀리면
        return False
    state = 1 # 괄호 상태 확인
    for b in s[1:]:
        if b == '(':  # 여는 괄호면 + 1
            state += 1
        else:         # 닫는 괄호면 - 1
            state -= 1
            if state < 0:  # 닫는 괄호가 앞의 여는 괄호보다 많으면 틀림
                return False
    if state == 0:  # 여는 괄호와 닫는 괄호의 수가 같으면
        return True
    else:
        return False

# 근데 스택 큐로도 원소 추가하고 빼는 식으로 풀 수 있을 것 같음