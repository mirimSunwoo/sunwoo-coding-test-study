#중복되는 문자 제거

def solution(characters):
    result = [characters[0]]
    for i in range(1,len(characters)):
        if characters[i-1] != characters[i]:
            result.append(characters[i]) #i-1로 되면 똑같은 문자를 추가하기 때문에 틀린것이다
    return ''.join(result)

print(solution("senteeenccccceeee"))