def solution(food):
    answer = '0'
    for idx in range(len(food)-1, 0, -1):
        cnt = food[idx]//2
        answer = str(idx)*cnt + answer + str(idx)*cnt
    return answer