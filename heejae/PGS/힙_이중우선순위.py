import heapq
def solution(operations):
    answer = []
    
    q = [] # 힙 만들기 ?
    
    for operation in operations:
        x, num = operation.split() 
        num = int(num)
        
        if x == 'I': 
            heapq.heappush(q, num) # 숫자 q에 넣음
        elif x == 'D' and num == 1:
            if len(q) != 0:
                max_value = max(q)
                q.remove(max_value) # 최댓값 빼버림
        else:
            if len(q) != 0:
                heapq.heappop(q) # 최솟값 빼버림
    
    if len(q) == 0:
        answer = [0, 0] # 다 돌고 안에 없으면 리턴
    else:
        answer = [max(q), heapq.heappop(q)] # 다 돌고 안에 있으면 리턴
        
    return answer
