'''
하루에 최소 한 개의 의상. 각 종류별로 하나만 가능
서로 다른 옷의 조합의 수는?
'''

def solution(clothes):
    answer = 1
    dic = {}
    for cloth in clothes:
        name, value = cloth[1], cloth[0]
        if name not in dic:
            dic[name] = 1
        dic[name] += 1
    for key in dic.keys():
        answer *= dic[key]
    return answer-1