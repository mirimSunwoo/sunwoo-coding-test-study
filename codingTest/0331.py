def solution(phone_number):
    answer = ''
    answer = len(phone_number[:-4])*"*" #뒷번호를 제외한 번호의 수를 세고 "*"로 치환한다
    return answer+phone_number[-4:] #answer + 뒷번호를 합쳐서 return 해준다

# 다른사람의 풀이
def hide_number(s):
    return "*"*(len(s)-4) + s[-4:]