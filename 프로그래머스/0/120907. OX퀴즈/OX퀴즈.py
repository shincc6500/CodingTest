def solution(quiz):
    answer = []
    for i in quiz:
        tmp = i.split()
        X = int(tmp[0])
        Y = int(tmp[2])
        Z = int(tmp[4])
        if '+' in tmp :
            if X+Y == Z:
                answer.append('O')
            else :
                answer.append('X')
        elif '-' in tmp:
            if X-Y == Z:
                answer.append('O')
            else :
                answer.append('X')        
    return answer