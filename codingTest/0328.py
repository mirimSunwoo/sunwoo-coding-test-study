# 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

# 방법1
def solution(num):
    if(num%2==0):
        return "Even"
    else:
        return "Odd"

#방법2
def solution(num):
    answer = ''
    if(num%2==0):
        answer = 'Even'
    elif(num%2==1):
        answer = 'Odd'
    return answer