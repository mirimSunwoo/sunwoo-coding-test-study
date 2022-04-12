def isIntList(answer):
    return int(answer)

def solution(n):
    answer = []
    nums = str(n)
    for x in range(len(nums),0,-1): #5,4,3,2,1
        answer += nums[x-1:x]
        newList = list(map(isIntList,answer))
    return newList