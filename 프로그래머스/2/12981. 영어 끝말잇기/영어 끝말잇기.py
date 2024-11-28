def solution(n, words):
    answer = []
    chance = 1
    num = 1
    used_word = set()
    c = words[0][0] #전 단어 마지막 글자. 
    for i in range(len(words)):
        if (words[i][0] != c or words[i] in used_word):
            return [num,chance]
        else:
            used_word.add(words[i])
            c = words[i][-1]
        if num == n:
            num = 1
            chance +=1
        else :
            num += 1
    return [0,0]
        