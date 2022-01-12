#학점별 인원수를 구하는 함수의 빈칸 채우기

def solution(scores):
    grade_counter = [0 for i in range(5)]
    for i in scores:
        if i>=85:
            grade_counter[0] +=1
        elif i>=70:
            grade_counter[1] +=1
        elif i>=55:
            grade_counter[2] +=1
        elif i>=40:
            grade_counter[3] +=1
        else:
            grade_counter[4] +=1
    return grade_counter

print(solution([30,77,65,90,67,54,67,88,43,67,99]))