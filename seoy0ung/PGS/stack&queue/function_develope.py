'''
각 기능은 진도가 100%일 때 서비스에 반영 가능
각 기능의 개발속도는 모두 달라 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있음
뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됨
작업의 진도가 적힌 정수 배열 / 각 작업의 개발 속도가 적힌 배열
각 배포마다 몇 개의 기능이 배포되는지를 return 하기
'''

def solution(progresses, speeds):
    answer = []
    cnt = 0  # 함께 배포가능한 기능 수 기록
    while progresses:  # 작업중인 기능이 있는 동안 실행
        for i in range(len(progresses)):
            progresses[i] += speeds[i]  # 각 진도에 속도만큼 더해주기
        while progresses:
            check = progresses.pop(0)  # 현재 기능
            speed = speeds.pop(0)  # 현재 작업속도
            if check >= 100:  # 완료된 작업이면
                cnt += 1  # 배포가능 기능 수 추가
                continue
            else:  # 완료되지 않았다면
                if cnt != 0:  # 배포가능한 기능이 있다면
                    answer.append(cnt)  # 배포
                progresses.insert(0,check)  # 다시 작업중인 목록 맨 앞에 추가
                speeds.insert(0, speed)
                cnt = 0  # 초기화
                break
        if cnt != 0:  # 전체를 다 돌았는데 초기화 안된 상태면 마지막에 추가
            answer.append(cnt)
    return answer