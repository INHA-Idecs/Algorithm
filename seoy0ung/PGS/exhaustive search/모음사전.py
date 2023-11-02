'''
사전에 알파벳 모음 A, E, I, O, U 만을 사용하여 만들 수 있는 길이 5 이하의 모든 단어가 수록
단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return
'''

from itertools import product
from functools import reduce

def solution(word):
    words = set()
    for i in range(1, 6):
        nPr = product(['A','E','I','O','U'], repeat=i)
        for w in nPr:
            w = reduce(lambda x, y: x+y, w, '')
            words.add(w)
    words = list(words)
    words.sort()
    return words.index(word) + 1