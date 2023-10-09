'''
각 기능은 진도가 100%일 때 서비스에 반영 가능
각 기능의 개발속도는 모두 달라 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있음
뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됨
작업의 진도가 적힌 정수 배열 / 각 작업의 개발 속도가 적힌 배열
각 배포마다 몇 개의 기능이 배포되는지를 return 하기
'''

def solution(progresses, speeds):
    answer = []
    cnt = 0
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses:
            check = progresses.pop(0)
            speed = speeds.pop(0)
            if check >= 100:
                cnt += 1
                continue
            else:
                if cnt != 0:
                    answer.append(cnt)
                progresses.insert(0,check)
                speeds.insert(0, speed)
                cnt = 0
                break
        if cnt != 0:
            answer.append(cnt)
    return answer