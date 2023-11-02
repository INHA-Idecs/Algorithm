'''
XX게임에는 피로도 시스템이 있음 (0 이상의 정수로 표현)
일정 피로도를 사용해서 던전을 탐험할 수 있음
- 최소 필요 피로도 : 각 던전마다 탐험을 시작하기 위해 필요한 최소한의 피로도
- 소모 피로도 : 던전 탐험을 마쳤을 때 소모되는 피로도
한 유저가 최대한 많이 탐험하려 함.
유저의 현재 피로도 k, 각 던전별 최소 피로도, 소모 피로도가 담긴 2차원 배열

- 현재 피로도보다 최소 피로도가 낮은 것 중에 소모 피로도가 적은 것
'''

# 순열로 해결
from itertools import permutations

def solution(k, dungeons):
    visits = []
    for permut in permutations(dungeons, len(dungeons)): # 던전 방문가능한 모든 순서
        answer = 0
        p = k
        for dung in permut:
            if p >= dung[0]:
                p -= dung[1]
                answer += 1
                if p < 0:
                    break
        visits.append(answer)
    return max(visits)