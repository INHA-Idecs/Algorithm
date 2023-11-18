"""
고속도로 이동하는 모든 차량이 단속카메라 한번은 만나도록 카메라 설치
최소 카메라 개수는?
"""


def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])  # 진출 시점 기준으로 정렬
    camera = -30001  # 초기 카메라 위치

    # 카메라 위치를 갱신하며 최소 카메라 개수를 찾음
    for route in routes:
        # 진입시점보다 카메라 위치가 작으면 진출시점(먼곳)에 추가
        if camera < route[0]:
            answer += 1
            camera = route[1]

    return answer