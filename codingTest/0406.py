def solution(s):
    answer = int(s)
    return answer

#다른사람의 풀이
def strToInt(str):
    result = 0

    for idx, number in enumerate(str[::-1]): #부호를 뽑아내는 반복문
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx) #정수로 바꾼 s와 자릿수를 곱하면서 누적합해준다

    return result