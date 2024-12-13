def solution(a, b):
    answer = 0
    # 분자의 약수 구하기
    tmp = []
    x = 2
    while a>1:        
        if a%x ==0:
            a = a//x
            tmp.append(x)
            x = 2
        else :
            x +=1
    # 분모 기약분수        
    for i in tmp:
        if b%i ==0:
            b = b//i
    #분모 소인수 분해
    tmp2 = set()
    while b>1:
        if b%x ==0:
            b = b//x
            tmp2.add(x)
            x = 2
        else :
            x +=1
    if 2 in tmp2:
        tmp2.remove(2)
    if 5 in tmp2:
        tmp2.remove(5)
        
    if len(tmp2) == 0:
        answer = 1
    else :
        answer = 2
    return answer