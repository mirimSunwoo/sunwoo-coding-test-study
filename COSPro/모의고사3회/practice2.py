#예산을 배분하기 위한 금액을 구하는 함수 빈칸 채우기(완료)

def func_a(arr):
    total = 0
    for i in arr:
        total += i
    return total

def solution(total, arr):
    result = []
    req_total = func_a(arr)
    for i in arr:
        if req_total > total :
            result.append(total//len(arr))
        else:
            result.append(i)
    return result

print(solution(500,[120,110,140,100]))
print(solution(500,[200,110,140,150]))