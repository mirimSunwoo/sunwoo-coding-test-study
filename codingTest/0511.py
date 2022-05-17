def solution(s):
    dict = {}
    e_num=['zero','one','two','three','four','five', 'six','seven','eight','nine']
    for i in range(10):
        dict[e_num[i]] = i
    print(dict)

    result = ''
    eng = ''
    for i in s:
        if i.isdigit():
            result = result+i
        elif i.isalpha():
            eng = eng+i
            if eng in dict.keys():
                result = result+str(dict[eng])
                eng = ''
    return int(result)

#다른사람의 풀이(블로그 참조)
def solution(s):
    e_num=['zero','one','two','three','four','five', 'six','seven','eight','nine']
    answer = ''
    for idx, num in enumerate(e_num):
        if num in s:
            s - s.replace(num,str(idx))
        answer = s
    return int(answer)