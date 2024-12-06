def solution(my_string):
    answer = ''
    erase_list = ['a','e','i','o','u']
    for x in erase_list:
        my_string = my_string.replace(x,'')

    return my_string