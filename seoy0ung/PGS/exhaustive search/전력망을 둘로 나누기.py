'''
n개의 송전탑이 전선을 통해 하나의 트리 형태로 연결
전선들 중 하나를 끊어서 현재의 네트워크를 2개로 분할
두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게.
포기데스요
'''

# 다른사람 풀이 : 집합자료형 사용. 이중 for문으로 모든 경우 탐색
def solution(n, wires):
    ans = n
    for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):  # i를 제거한 새로운 리스트 생성
        s = set(sub[0])
        # 해당 노드와 연결 된 노드가 있으면 업데이트
        [s.update(v) for _ in sub for v in sub if set(v) & s]  # 집합연산자 & : 교집합 연산,   집합연산자 update : 여러데이터를 한번에 추가
        ans = min(ans, abs(2 * len(s) - n))  # 더 작은 절대값차이 저장
    return ans