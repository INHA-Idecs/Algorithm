'''
운영체제가 다음 규칙에 따라 프로세스를 관리할 경우 특정 프로세스가 몇 번째로 실행되는지 알아보자
1. 실행 대기 큐에서 대기중인 프로세스 하나를 꺼냄
2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣음
3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스 실행
 3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됨

'''

def solution(priorities, location):
    target = priorities[location]  # 특정 프로세스의 우선순위 정보
    loc = [i for i in range(len(priorities))]  # 같은 우선순위를 가진 것과 구분하기 위해 현재 위치 정보를 인덱스로 기록
    answer = 0
    while priorities:  # 프로세스 남아있다면 실행
        highest = max(priorities)  # 현재 실행가능한 프로세스
        process = priorities.pop(0)  # 가장 앞에 있는 프로세스
        n_loc = loc.pop(0)  # 현재 프로세스의 처음 위치정보(구분위함)
        if process == highest:  # 실행가능한 프로세스라면
            answer += 1
            if target == process and location == n_loc:  # 실행한 프로세스가 타겟 프로세스라면 종료
                return answer
        else:  # 실행 불가능한 경우 다시 맨 뒤로 집어넣음
            priorities.append(process)
            loc.append(n_loc)
    return answer