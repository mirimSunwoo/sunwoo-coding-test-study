'''
교차점의 개수를 구하는 함수 빈칸 채우기
'''
def solution(left_rings):
    answer = 0
    for i in range(len(left_rings)): #왼쪽 고리 번호, left_rings[1] : 오른쪽 번호로
        if left_rings[i] <= i:       #1. 왼쪽/=오른쪽
            for k in range(i):
                if left_rings[k] > left_rings[i]:#1. 왼쪽\오른쪽
                    answer += 1
    return answer

#왼쪽\오른쪽 and 왼쪽/오른쪽
#왼쪽/오른쪽 and 왼쪽\오른쪽
print(solution([0,3,1,4,2])) #3
print(solution([3,1,2,4,0])) #6
