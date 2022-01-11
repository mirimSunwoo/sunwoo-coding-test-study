'''
거스름돈을 계산가흔 함수 작성
'''

def solution(price, money):
    answer = 0
    total = sum(price)
    if money>total:
        answer = money - total
    else:
        return -1
    return answer


price = [2100,3200,2100,800]
print(solution(price,10000))