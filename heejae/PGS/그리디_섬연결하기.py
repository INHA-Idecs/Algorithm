def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2]) # 비용기준으로 오름차순 정렬
    connect = set([costs[0][0]]) # 연결을 확인하는 집합
    
    ## Kruskal 알고리즘으로 최소 비용 구하기
    # 그래프의 간선들을 가중치의 오름차순으로 정렬한다.
    # 정렬된 간선 리스트에서 순서대로 사이클을 형성하지 않는 간선을 선택한다.
    # 즉, 가장 낮은 가중치를 먼저 선택한다.
    # 사이클을 형성하는 간선을 제외한다.
    # 해당 간선을 현재의 MST(최소 비용 신장 트리)의 집합에 추가한다.
    
    while len(connect) != n:
        for cost in costs:
            # 간선의 양쪽 끝 노드가 모두 이미 연결된 상태면 사이클을 형성하므로 넘어감
            if cost[0] in connect and cost[1] in connect:
                continue
            # 간선의 한쪽 끝 노드만 연결되어 있으면 해당 간선을 추가하고 연결된 노드 집합을 갱신
            if cost[0] in connect or cost[1] in connect:
                # 연결된 노드 집합에 현재 간선의 양 끝 노드를 추가
                connect.update([cost[0], cost[1]])
                answer += cost[2]
                break
                
    return answer
