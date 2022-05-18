def solution(arr):
    answer = []
    saveNum = -1
    for i,arr_num in enumerate(arr):
        if saveNum != arr[i]:
            answer.append(arr_num)
            saveNum=arr[i]
        else:
            pass
    return answer