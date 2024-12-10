def solution(my_string):
    answer = 0
    tmp = my_string.split()
    answer += int(tmp[0])
    for i in range(1,len(tmp),2):
        if tmp[i] == '+':
            answer += int(tmp[i+1])
        else :
            answer -= int(tmp[i+1])
        
    return answer