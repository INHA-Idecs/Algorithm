"""
구명보트를 이용해서 구출하기!
최대 2명, 무게제한에 맞춰서 구명보트 최대한 적게 사용하기
무거운 사람 + 가벼운 사람 조합으로 확인
"""


def solution(people, limit):
    answer = 0
    people.sort()

    start = 0
    end = len(people) - 1
    while start < end:
        # 같이 탈 수 있는지 확인. 같이 탄 횟수 기록
        if people[start] + people[end] <= limit:
            answer += 1
            start += 1
        # 안되면 혼자 나가기
        end -= 1

    # 전체 횟수에서 같이 탄 횟수만큼 빼기
    return len(people) - answer