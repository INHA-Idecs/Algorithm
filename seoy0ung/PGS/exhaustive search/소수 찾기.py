'''
소수 찾기
흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지?

'''

from itertools import permutations  # 순열 만드는 함수
import math
from functools import reduce  # 튜플 합쳐주는 함수

def solution(numbers):
    answer = 0
    nums = set()
    for i in range(1, len(numbers)+1):  # 만들 수 있는 순열 생성
        nPr = permutations(numbers,i)
        new = set(nPr)  # 중복 제거
        for t in new:
            num = reduce(lambda x, y: x+y, t, '')  # 합쳐서 숫자로
            if int(num) <= 1:
                continue
            nums.add(int(num))

    for num in nums:
        check = False  # 소수인지 판별
        for i in range(2, int(math.sqrt(num))+1):  # 제곱근까지에 대해서 안나눠지면 소수
            if num % i == 0:
                check = True
                break
        if check == False:  # 소수 아니면 1 더해줌
            answer += 1
    return answer