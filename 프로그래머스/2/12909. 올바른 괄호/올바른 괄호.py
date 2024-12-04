def solution(s):
    a = 0
    for i in s:
        if i == '(':
            a +=1
        elif i == ')':
            a -= 1
        if a<0 :
            return False
    if a == 0:
        return True
    else : 
        return False
            
        