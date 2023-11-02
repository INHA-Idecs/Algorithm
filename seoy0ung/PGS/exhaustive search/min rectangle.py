'''
최소 직사각형
모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기 return
'''

def solution(sizes):
    w = []
    h = []
    for size in sizes:
        x, y = size[0], size[1]
        if x > y:
            w.append(x)
            h.append(y)
        else:
            w.append(y)
            h.append(x)
    return max(w)*max(h)