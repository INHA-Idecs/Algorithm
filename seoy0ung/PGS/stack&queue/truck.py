'''
트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 함
모든 트럭이 다리를 건너는데 최소 몇 소가 걸리는지 알아내기
bridge_length 대 올라갈 수 있음
weight 이하까지의 무게를 견딜 수 있음
다리에 완전히 오르지 않은 트럭의 무게는 무시
'''

# deque 사용 (효율성 증가 O(1))
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0  # 총 걸린 시간
    w = 0  # 현재 무게
    bridge = deque([0]*bridge_length)  # 트럭 위치와 무게 정보
    truck = deque(truck_weights)
    while truck:  # 트럭이 남아있는 동안
        time += 1

        # 위치 하나씩 이동. 현재 무게에서 빠진 트럭 무게 빼주기
        w -= bridge.popleft()
        # 새로 추가할 트럭 정보
        new = truck.popleft()

        if w + new <= weight:  # 다리에 트럭 추가할 수 있으면 추가.
            bridge.append(new)
            w += new
        else:                  # 추가할 수 없으면 0 추가
            truck.appendleft(new)
            bridge.append(0)

    return time + bridge_length # 마지막으로 올라간 트럭이 다리를 빠져나와야 함