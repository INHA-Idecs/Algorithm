'''
- 운영체제의 프로세스들에 대한 queue가 있음
- top에 위치하는 프로세스는 queue에서 우선순위가 자기보다 높은 게 없을 때에만 실행 가능(있으면 맨 뒤로)
- location으로 지정한 프로세스가 몇 번째로 실행되는지 알고싶음
'''

from collections import deque

def solution(priorities, location):
    answer = 1
    q = deque(priorities)
    while len(q) != 0:
        if  max(q) <= q[0]: # 뒤에 우선순위 높은게 없음
            if location == 0:
                return answer
            q.popleft()
            answer = answer + 1
            location = location - 1
        else: # 뒤에 우선순위 높은게 있음
            q.append(q.popleft())
            if location == 0: # 알고싶은 프로세스 차례인 경우
                location = len(q) - 1
            else: # 알고싶은 프로세스 차례가 아닌 경우
                location = location - 1

    return answer
