from itertools import permutations
import math

def isDecimal(num):
    if(num <= 1):
        return False 
    #에라토스테네스의 체
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False    
    return True
    
def solution(numbers):
    
    numlist = list(numbers)
    ansnums = set()
    for i in range(1, len(numbers)+1):
        permutationList = permutations(numlist, i) # 숫자 조합 만들기
        for j in permutationList:
            ansnum = int(''.join(j))
            ansnums.add(ansnum)

    
    count = 0
    for k in ansnums:
        if isDecimal(k): # 소수 판별
            count += 1
            
    return count
