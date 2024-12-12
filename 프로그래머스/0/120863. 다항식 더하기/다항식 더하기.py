def solution(polynomial):
    answer = ''
    counter = 0
    num = 0
    tmp = polynomial.replace('+','')

    tmp = tmp.split()

    for i in tmp:
        if 'x' in i:
            if len(i) ==1:
                counter +=1
            else:                
                counter += int(i[:-1])
        else: 
            num += int(i)

    
    if counter == 0:
        answer = f'{num}'
    elif counter == 1:
        if num == 0:
            answer = 'x'
        else:
            answer = f'x + {num}'
    elif num == 0:
        answer = f'{counter}x'
    else:
        answer = f'{counter}x + {num}'
    return answer