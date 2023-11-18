def solution(n, times):
    # 이진 탐색을 위한 시작점과 끝점을 설정
    # 시작점은 1이고, 끝점은 가장 오래 걸리는 심사 시간(max(times))과 전체 인원 수(n)의 곱으로 설정
    start, end = 1, max(times) * n
    answer = end
    while start <= end:
        mid = (start + end) // 2
        
        people = 0
        for time in times:
            people += (mid // time)
            
        if people < n:
            start = mid+1
        else:
            end = mid-1
            answer = min(answer, mid)
            
    return answer
