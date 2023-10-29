from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for i in permutations(dungeons, len(dungeons)):
        hp = k
        count = 0 
        
        for j in i:
            if hp >= j[0]:
                hp -= j[1]
                count += 1
            
            if count > answer:
                answer = count
    
    return answer
