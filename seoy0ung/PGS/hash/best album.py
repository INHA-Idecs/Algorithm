'''
장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범 출시
고유 번호로 구분
1. 속한 노래가 많이 재생된 장르를 먼저 수록
2. 장르 내에서 많이 재생된 노래를 먼저 수록
3. 장르 내에서 재생 횟수가 같은 노래 중 고유 번호가 낮은 노래를 먼저 수록
'''

def solution(genres, plays):
    album = {}
    total = {}
    answer = []
    for i in range(len(genres)):
        if genres[i] not in album:
            album[genres[i]] = {i:plays[i]}
            total[genres[i]] = plays[i]
        else:
            album[genres[i]][i] = plays[i]
            total[genres[i]] += plays[i]
    total = sorted(total.items(), key = lambda x:x[1], reverse=True)
    for info in total:
        genre = info[0]
        count = sorted(album[genre].items(), key=lambda x:(x[1],-x[0]))
        i = 0
        while count:
            if i == 2:
                break
            answer.append(count.pop()[0])
            i += 1
    return answer