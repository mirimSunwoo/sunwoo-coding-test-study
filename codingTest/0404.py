def solution(a, b):
    answer = 0 #최종변수를 담을 answer를 0으로 초기화 한다
    add = 0 #내젹을 담을 변수를 만든다
    for x in range(len(a)): #a와b배열의 길이가 같으므로 a배열의 길이만큼 반복한다
        add = a[x] * b[x] #1부터 a배열길이만큼 배열의 값을 꺼내서 내적한다
        answer += add #최종변수에 add를 누적한다
    return answer

#다른사람의 풀이
def solcution(a,b):
    return sum([x*y for x,y in zip(a,b)])

#zip 함수 : 각 객체가 담고있는 원소를 터플의 현태로 차례로 접근할 수 있는 반복자를 반환
# (예시) : 양쪽의 지퍼를 올리는 것처럼 양 측에  테이터를 하나씩 차례대로 짝을 지어준다