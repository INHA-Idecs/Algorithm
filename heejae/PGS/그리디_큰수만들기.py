def solution(number, k):
    answer = []

    for i in number:
        while k > 0 and answer and answer[-1] < i: # 앞 숫자가 뒤 보다 크면 뒷 숫자 제거
            answer.pop()
            k -= 1
        answer.append(i) # 앞에서 부터 추가

    return ''.join(answer[:len(answer) - k]) # 제거하지 못한 같은 숫자를 남은 k만큼 빼줌
