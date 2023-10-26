import heapq

# heapq.heapify() 리스트를 힙으로 변환
# heapq.heappush(heap, item) item 값을 heap으로 푸시
# heapq.heappop(heap) heap에서 가장 작은 항목을 팝하고 반환
# heapq.heapreplace(heap, item) heap에서 가장 작은 항목을 팝하고 반환하며, 새로운 item도 푸시

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        melt = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, melt)
        answer += 1
        if scoville[0] < K and len(scoville) == 1:
            return -1

    return answer
