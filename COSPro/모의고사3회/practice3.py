#가장 많이 같은 반을 보낸 학생 찾는 함수 작성하기

def solution(table):
    answer = 0
    student = []
    for i in range(1,6):
        cnt = 0
        for j in range(5):
            if table[0][j] == table[i][j]:
                cnt += 1
        student.append(cnt)
    maxinum = student[0]
    answer = 0
    for index, cnt in enumerate(student):
        if maxinum < cnt:
            maxinum = cnt
            answer = index + 1
    return answer

table = [
    [2,6,1,7,3], #선생님
    [2,9,4,6,8], #학생1
    [6,3,4,7,1], #학생2
    [7,7,1,1,2], #학생3
    [8,6,9,7,3], #학생4
    [4,6,5,9,2]  #학생5
]
print(solution(table))