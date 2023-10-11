'''
초 단위로 기록된 주식가격이 담긴 배열 prices
가격이 떨어지지 않은 기간은 몇 초인지 return
'''

# 스택 안쓰고
def solution(prices):
    answer = [0]*len(prices)
    # 각 가격에 대해 뒷 시간의 가격이 같거나 더 클때 1 더해주기. 마지막이 아니라면 자신을 포함해서 1 더해줌
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

# 스택 쓰고 (근데 이해가 안감)
def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        while stack and stack[-1][1] > prices[i]:
            past, _ stack.pop()
            answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer