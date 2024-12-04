def solution(hp):
    answer = 0
    
    while True:
        if hp >=5 :
            hp -=5
            answer += 1
        elif hp>=3:
            hp -= 3
            answer += 1
        elif hp>=1:
            hp -= 1
            answer += 1
        if hp == 0:
            break
    return answer