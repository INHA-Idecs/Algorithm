def solution(n, wires):
    answer = n
    
    for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))): # 모든 전선 조합에 대한 루프
        s = set(sub[0]) # 각 조합에 대해 첫 번째 전선으로 구성된 집합 s를 만듬.
        [s.update(v) for _ in sub for v in sub if set(v) & s] # 여기서 s 집합에 대해 다른 전선들을 추가. 중복된 원소가 있을 경우 추가.
        answer = min(answer, abs(2 * len(s) - n)) # 현재까지의 그룹 나누기에서 나온 두 그룹의 크기 차이를 계산
    
    return answer
