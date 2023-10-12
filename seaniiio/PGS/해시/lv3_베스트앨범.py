'''
- 장르별로 가장 많이 재생된 두 곡씩 뽑아서 “베스트 앨범”을 만들어야 함
- 이 때, 수록할 곡의 순서를 고려해야 함
1. 속한 노래들의 재생횟수 합이 가장 큰 장르를 먼저
2. 같은 장르 내에서는 재생횟수가 큰 노래를 먼저, 같다면 고유번호(입력된 순서)가 작은 노래를 먼저
'''

def solution(genres, plays):
    answer = []
    # 장르를 key로, 그 장르에 속하는 노래들의 정보를 value로 하는 딕셔너리.
    # key:value => 'pop' : [500(장르의 총 재생수), [500, 0(고유번호)]]
    albums = {}
    for i in range(len(genres)):
        if genres[i] not in albums:
            albums[genres[i]] = [plays[i]]
            albums[genres[i]].append([[plays[i], i]]) 
        else:
            albums[genres[i]][0] = albums[genres[i]][0] + plays[i]
            albums[genres[i]].append([[plays[i], i]])
            
    albums = sorted(albums.values(), key=lambda x : x[0], reverse=True) # 노래 재생 기준으로 장르 정렬
    for i in range(len(albums)): # 장르 개수만큼
        song_list = albums[i][1:]
        song_list_ordered = sorted(song_list, key=lambda x : x[0][0], reverse=True)
        answer.append(song_list_ordered[0][0][1])
        if len(song_list) > 1 : answer.append(song_list_ordered[1][0][1])
    return answer

'''
정렬을 잘 해야함
첫 번째는 장르를 정렬하는 것이고, 정렬 조건은 노래의 총 재생 횟수
두 번째는 각 장르에서 노래를 정렬하는 것이고, 정렬 조건은 노래별 재생 횟수
'''

# 시간 복잡도: O(n) + O(nlogn) (+ O(klogk))
