from itertools import permutations

def solution(k, dungeons):
    answer = 0
    dun_len = len(dungeons)
    
    for permute in permutations(dungeons, dun_len):
        count = 0
        hp = k
        
        for i in permute:
            # print(i)
            if hp >= i[0]:
                hp -= i[1]
                count +=1
            if answer < count:
                answer = count
                
    return answer