'''
- 개발해야 하는 여러 기능들이 존재
- 진행 상황과 진행 속도가 각기 다름
- 뒤에있는 기능이 앞의 기능보다 먼저 개발되더라도 앞의 기능이 완성되어야 배포 가능
- 따라서 “현재 가장 우선순위가 높은 기능의 현황”만 추적하면 됨
'''

from collections import deque
def solution(progresses, speeds):
    q = deque(progresses)
    speeds_q = deque(speeds)
    answer = []
    while len(q) != 0:
        for i in range(len(q)):
            q[i] = q[i] + speeds_q[i]
        if q[0] >= 100:
            count = 1
            q.popleft()
            speeds_q.popleft()
            while len(q) != 0 and q[0] >= 100:
                count = count + 1
                q.popleft()
                speeds_q.popleft()
            answer.append(count)
    return answer


# 인덱스 이용
# 작업속도, 속도 두 개의 큐를 건들(pop해줄) 필요 없이, 그냥 인덱스 하나만 이동하면 됨.
def solution(p, s):
    answer = []
    top_index = 0 # 현재(top) 인덱스
    while top_index < len(p):
        for i in range(len(p)):
            p[i] = p[i] + s[i]
        if p[top_index] >= 100:
            count = 1
            top_index = top_index + 1
            while top_index < len(p) and p[top_index] >= 100:
                count = count + 1
                top_index = top_index + 1
            answer.append(count)
    return answer
