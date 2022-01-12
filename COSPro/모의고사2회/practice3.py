#방문객 수의 차이를 구하는 함수의 빈칸 채우기

def func_a(arr,num):
    ret = []
    for i in arr:
        if i != num: #...?이게 뭘까나
            ret.append(i)
    return ret
def func_b(a,b):
    if a>b:
        return a-b
    else:
        return b-a
def func_c(arr):
    ret = -1
    for i in arr:
        if ret<i:
            ret = i
    return ret

def solution(visitor):
    max_first = func_c(visitor)
    visitor_removed = func_a(visitor, max_first)
    max_second = func_c(visitor_removed)
    answer = func_b(max_first,max_second)
    return answer

print(solution([32,45,67,84,12,45,65,43,67,88]))