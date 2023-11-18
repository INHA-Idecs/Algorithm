"""
체육복이 도난당한 학생에게 여분을 가진 학생이 앞뒤번호 학생에게 체육복을 빌려줄 수 있다
체육수업을 들을 수 있는 학생의 최댓값은?

전체 학생 수 n
도난당한 학생 번호 lost
여벌 체육복 학생 번호 reserve
"""

def solution(n, lost, reserve):
    # 뒷번호 학생이 먼저 나올 수 있기 때문에 정렬해줌. 안하면 테스트케이스 18 20 실패
    # 여분을 가져온 학생도 잃어버릴 수 있으므로, 해당 학생은 양쪽 리스트에서 제거해줌
    _reserve = sorted([r for r in reserve if r not in lost])
    _lost = sorted([l for l in lost if l not in reserve])

    # 여벌 가져온 학생 기준으로, 앞번호 학생 먼저 확인
    for i in _reserve:
        b = i-1
        a = i+1
        if b in _lost:
            _lost.remove(b)
        elif a in _lost:
            _lost.remove(a)
            
    # 전체에서 수업 못듣는 학생 제거
    return n-len(_lost)