def solution(my_string, num1, num2):
    answer = ''
    my_string = list(my_string)
    temp = my_string[num1]
    my_string[num1] = my_string[num2]
    my_string[num2] = temp
    answer = answer.join(my_string)
    return answer
