"""
n개의 섬 사이의 다리를 건설하는 비용(costs)
모든 섬이 서로 통행가능하도록 만든 최소 비용은?
"""


def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])  # 비용기준으로 오름차순 정렬
    connect = set([costs[0][0]])  # 연결을 확인하는 집합

    # Kruskal 알고리즘으로 최소 비용 구하기
    while len(connect) != n: # 모든 섬이 연결될때까지
        for cost in costs:
            # 모두 들어있으면 패스
            if cost[0] in connect and cost[1] in connect:
                continue

            # 연결 안 되어있으면 추가
            if cost[0] in connect or cost[1] in connect:
                connect.update([cost[0], cost[1]])
                answer += cost[2]
                break

    return answer
