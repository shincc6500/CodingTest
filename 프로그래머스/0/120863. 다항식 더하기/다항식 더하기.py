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
                i = i.replace('x','')
                counter += int(i)
        else: 
            num += int(i)

    
    if counter == 0:
        answer = f'{num}'
    elif num == 0:
        if counter == 1:
            answer = 'x'
        else:
            answer = f'{counter}x'
    elif counter == 1:
        answer = f'x + {num}'
    else:
        answer = f'{counter}x + {num}'
    return answer