#특정값보다 작은 값을 찾는 함수 수정하기
#평균보다 작은 수의 개수 찾기
def solution(data):
    total = 0
    for i in data:
        total += i
    cnt = 0
    average = total//len(data)
    for i in data:
        if i<average:
            cnt += 1
    return cnt

print(solution([1,2,3,4,5,6,7,8,9,10]))