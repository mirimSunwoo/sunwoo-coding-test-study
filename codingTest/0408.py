def solution(n):
    answer = str(n) #매개변수를 문자열로 변환한다
    total = 0 #자릿수 누적을 할 변수
    for x in range(len(answer)): #자릿수만큼 반복한다
        total += int(answer[x]) #문자열 함수의 자릿수를 int로 변환하여 누적합 한다
    return total

#다른사람의 풀이
def sum_digit(number):
    return sum([int(i) for i in str(number)]) #누적합보다 sum함수를 사용하여 자릿수를 더해주었다
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123))); #format을 사용한것이 인상적이다