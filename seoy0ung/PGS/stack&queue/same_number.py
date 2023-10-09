'''
배열 arr의 각 원소는 숫자 0부터 9까지로 이루어짐
배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거
arr의 순서 유지해야함
'''

def solution(arr):
    same = arr[0]
    answer = [same]
    for i in arr:
        if same == i:
            continue
        else:
            answer.append(i)
            same = i
    return answer