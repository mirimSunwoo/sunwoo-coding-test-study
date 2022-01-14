#You may use import as below.
#import math
# (완료)

def solution(shirt_size):
    #Write code here.
    answer = [0 for _ in range(6)]
    for x in shirt_size:
        if x == "XS":
            answer[0] += 1
        elif x == "S":
            answer[1] += 1
        elif x == "M":
            answer[2] += 1
        elif x == "L":
            answer[3] += 1
        elif x == "XL":
            answer[4] += 1
        elif x == "XXL":
            answer[5] += 1
    return answer

#The following is code to output testcase.
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size);

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")