'''
단 한명의 마라톤을 완주하지 못한 선수의 이름을 return하자!
동명이인이 있을 수 있다

* 동명이인을 처음에 잡아내지 못했다 ㅠ
* 중간에 찾았을 때 for문을 break로 탈출해야 효율성에 안걸린다.
'''

def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    answer = participant[-1]
    for i in range(len(participant)-1):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    return answer