def solution(people, limit) :
    answer = 0
    people.sort()
    
    while len(people) > 1:
        if people[0] + people[-1] <= limit:
            people.pop(0)
            people.pop(-1)
        else:
            people.pop(-1)
        answer += 1
    if len(people) == 1:
        answer += 1
    return answer
