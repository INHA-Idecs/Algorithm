def solution(brown, yellow):
    answer = []
    
    def getDivisor(n): # 약수 리스트 구하기
        divisors = []
        for i in range(1, int(n**(1/2)) + 1):
            if (n % i == 0):
                divisors.append(i)
        divisors.sort()
        return divisors
    
    yel_div = getDivisor(yellow)
    for i in yel_div:
        if ((i + (yellow / i)) * 2 + 4) == brown: # 브라운 = 옐로의 가로세로 x 2 + 모서리 네 개
            answer.append(yellow / i + 2)
            answer.append(i + 2)
    
    return answer 
