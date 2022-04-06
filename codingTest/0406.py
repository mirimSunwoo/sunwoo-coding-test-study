def solution(s):
    answer = int(s) #문자열을 int형으로 감싸서 형변환 시켰다
    return answer

#다른사람의 풀이
def strToInt(str):
    result = 0 #변수 초기화

    for idx, number in enumerate(str[::-1]): #부호를 뽑아내는 반복문(첫번째 자리)
        if number == '-': #만약 부호가 -라면
            result *= -1 #값에 -를 곱해 음수로 만든다
        else: #만약 양수라면
            result += int(number) * (10 ** idx) #정수로 바꾼 s와 자릿수를 곱하면서 누적합해준다

    return result