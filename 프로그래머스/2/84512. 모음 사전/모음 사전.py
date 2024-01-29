from itertools import product

def solution(word):
    words = []
    arr = ["A","E","I","O","U"]
    
    for i in range(5):
        for pr in product(arr,repeat=i+1):
            words.append(''.join(pr))
    # print(words)
    words.sort()
    
    return words.index(word) + 1 
            
    