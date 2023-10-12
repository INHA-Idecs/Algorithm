'''
괄호가 모두 올바르게 짝지어져야 한다.
'()'으로 만났을 때 짝지어졌다고 판단하고 pop한다.
마지막에 스택에 뭔가 남아있다면 제대로 짝지어지지 않은 것으로 판단한다.
'''

def solution(s):
    answer = True
    stk = []
    for c in s:
        if len(stk) == 0:
            stk.append(c)
        elif c == ')' and stk[-1] == '(': # 짝이 맞는 경우
            stk.pop()
        else:
            stk.append(c)
    if len(stk) != 0 : answer = False
    return answer

