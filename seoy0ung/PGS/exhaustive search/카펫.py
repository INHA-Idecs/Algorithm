'''
중앙에는 노란색 테두리 1줄은 갈색
갈색 격자 수, 노란색 격자 수 주어질 때 카펫의 가로, 세로 크기는?
'''
def solution(brown, yellow):
    y_area = (brown-4)//2
    nums = []
    for i in range(1, y_area//2+1):
        nums.append([i, y_area-i])
    print(nums)
    for num in nums:
        x, y = num[0], num[1]
        if x*y == yellow:
            if x >= y:
                return [x+2, y+2]
            else:
                return [y+2, x+2]