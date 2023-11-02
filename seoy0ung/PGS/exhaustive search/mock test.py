'''
모의고사
1번 수포자 : 1 2 3 4 5
2번 수포자 : 2 1 2 3 2 4 2 5
3번 수포자 : 3 3 1 1 2 2 4 4 5 5

정답이 순서대로 들은 배열 주어졌을 때, 가장 많은 문제를 맞춘 사람 return
'''


def solution(answers):
    student = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    answer = []
    max = 0

    for i in range(3):
        score = 0
        idx = len(student[i])
        for j in range(len(answers)):
            if answers[j] == student[i][j % idx]:
                score += 1
        if max < score:
            answer = [i + 1]
            max = score
        elif max == score:
            answer.append(i + 1)
    return answer