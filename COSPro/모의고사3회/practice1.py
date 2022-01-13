#거리 차이를 구하는 함수 빈칸 채우기

def solution(a,b):
    answer = 0
    diff = (a-b) if a>b else b - a
    answer = 10 /diff
    return answer * 60

print(solution(10,1))