'''
5
카페 회원들에게 일련번호 부여
가장 많은 글을 작성한 회원의 글 개수는 가장 적게 작성한 회원의 글 개수가 몇 배인지
1. 리스트에 들어있는 각 회원별 글 개수를 셉니다.
2. 가장 많이 작성한 회원의 글 개수를 구합니다.
3. 가장 적게 작성한 회원의 글 개수를 구합니다.
4. 가장 많이 작성개수가 가장 적게 작성한 개수보다 몇 배인지 구함
'''
def func_a(arr):
    counter=[0 for _ in range(1001)]
    for i in arr:
        counter[i] += 1
    return counter
def func_b(arr):
    ret=0
    for i in arr:
        if ret<i:
            ret=i
    return ret
def func_c(arr):
    ret = func_b(arr) #최댓값을 구한것을 ret에넣어놓는다
    for i in arr:
        if i != 0 and ret>i:
            ret = i
    return ret
def solution(arr):
    counter=func_a(arr)
    max_cnt=func_b(counter)
    min_cnt=func_c(counter)
    return max_cnt // min_cnt

print(solution([105,655,555,5]))