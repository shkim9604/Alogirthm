def solution(numbers):
    answer = ""
    eng = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "zero": "0"}
    string = ""
    for i in numbers:
        string += i
        if string in eng:
            answer += eng[string]
            string = ""
    answer = int(answer)
    return answer
