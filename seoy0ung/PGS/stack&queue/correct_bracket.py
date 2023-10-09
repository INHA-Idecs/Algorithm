'''
올바른 괄호면 true 리턴, 올바르지 않으면 false 리턴하는 solution
'''

def solution(s):
    now = s[0]
    if now != '(':
        return False
    state = 1
    for b in s[1:]:
        if b == '(':
            state += 1
        else:
            state -= 1
            if state < 0:
                return False
    if state == 0:
        return True
    else:
        return False