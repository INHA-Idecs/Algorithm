def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # routes를 차량이 나간 지점 (진출) 기준으로 정렬
    camera = -30001 # -30001부터 카메라 위치를 찾기

    for route in routes:
        # 현재 카메라의 위치가 해당 차량이 진입한 지점보다 작으면, 새로운 카메라를 설치
        if camera < route[0]:
            answer += 1
            # 현재 카메라의 위치를 해당 차량이 나간 지점으로 업데이트
            # 이는 현재 카메라로 감시된 차량은 더 이상 고려하지 않아도 된다는 것을 의미
            camera = route[1]
    return answer
