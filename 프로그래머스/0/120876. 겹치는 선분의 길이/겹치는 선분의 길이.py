def solution(lines):
    answer = 0
    tmp = []
    for i in lines:
        for j in range(i[0],i[1]):
            tmp.append(j)
    tmp2 = set(tmp)
    for i in tmp2:
        if tmp.count(i)>1:
            answer +=1
        
    return answer