'''
하드디스크는 한 번에 하나의 작업만 수행.
일반적인 방법은 요청이 들어온 순서대로 처리하는 것이지만...
작업 요청 시점과 작업 소요시간 담은 2차원 배열이 주어질 때
작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마나 되는지?

- 각 작업의 대기시간 : 현재 시각에서 요청시간 뺀 시간.
- 작업 시작하면 처리시간 더해줘서 시점 이동
- 작업 종료시점 기준으로 처리시간이 짧은거 먼저 처리
'''

import heapq


def solution(jobs):
    answer, time, i = 0, 0, 0
    heap = []
    start = -1

    while i < len(jobs):
        for info in jobs:
            if start < info[0] <= time:
                heapq.heappush(heap, (info[1], info[0]))  # 실행시간, 요청시간 순
        if len(heap) > 0:
            new = heapq.heappop(heap)
            start = time
            time += new[0]
            answer += (time - new[1])
            i += 1
        else:
            time += 1
    return int(answer / len(jobs))