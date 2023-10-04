'''
N 마리의 폰켓몬 중 N/2 마리를 선택할 때 가장 많은 종류를 얻을 수 있도록 한다면
폰켓몬 종류 번호의 개수는?
'''

def solution(nums):
    choice = len(nums)//2
    kind = len(set(nums))
    if kind >= choice:
        answer = choice
    else:
        answer = kind
    return answer