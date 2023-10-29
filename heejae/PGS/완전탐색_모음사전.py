from itertools import product

def solution(word):
    words = []
    for i in range(1, 6):
        for j in product(['A', 'E', 'I', 'O', 'U'], repeat = i): # 중복순열 진짜 이거라고 ?
            words.append(''.join(list(j)))

    words.sort()
    return words.index(word) + 1 # 리스트 내 위치 찾기 (인덱스 + 1)
