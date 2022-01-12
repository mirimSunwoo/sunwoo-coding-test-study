'''
관세를 매긴 금액을 구하는 함수 작성하기
'''
def solution(price, grade):
    answer = 0
    if grade == "S":
        answer = price * 0.05
    elif grade == "G":
        answer = price * 0.1
    elif grade == "V":
        answer = price * 0.15
    return int(price +answer)

print(solution(1000,"S"))