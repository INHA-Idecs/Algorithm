'''
모든 음식의 스코빌 지수를 K 이상으로.
스코빌 지수가 가장 낮은 두 개의 음식을 섞어 새로운 음식 만듦
'''

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K:
        new = heapq.heappop(scoville)
        if scoville:
            new += heapq.heappop(scoville) * 2
            heapq.heappush(scoville, new)
            answer += 1
        else:
            return -1
    return answer