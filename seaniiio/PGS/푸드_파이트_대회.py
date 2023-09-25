def solution(food):
    answer = '0'
    n = len(food)
    for i in range(len(food) - 1 , 0, -1):
        food_n = food[i] // 2
        answer = (str(i) * food_n + answer + str(i) * food_n)
    return answer