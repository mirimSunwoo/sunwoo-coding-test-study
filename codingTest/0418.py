def solution(arr):
    sort = []
    remove = min(arr)
    for i in arr:
        if i == remove:
            print(i)
            arr.remove(i)
    if len(arr) == 0:
        arr.append(-1)
    return arr

#다른 사람의 풀이
def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)]