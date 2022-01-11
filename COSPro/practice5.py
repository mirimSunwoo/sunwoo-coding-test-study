'''
정수에 3,6,9가 포함되어 있는지 확인하는 함수의 빈칸 채우기
'''
def solution(number):
    count = 0
    for i in range(1,number+1):
        current = i
        while current != 0:
            unit = current % 10
            if unit == 3 or unit ==6 or unit ==9:
                count +=1
            current = current//10
    return count

print(solution(12))