import heapq

def solution(operations):
    heap = []
    for cmd in operations:
        op, num = cmd.split()
        if op == "I":
            heapq.heappush(heap, int(num))
        else:
            if len(heap) == 0:
                continue
            elif num == '1':
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
            else:
                heapq.heappop(heap)
    if len(heap) == 0:
        return [0,0]
    else:
        return [max(heap), min(heap)]