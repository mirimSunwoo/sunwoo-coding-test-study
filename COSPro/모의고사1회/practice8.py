#거꾸로 읽어도 같은 문자

def solution(sentence):
    filtered = []
    for s in sentence:
        if s != ' ' and s  != '.':
            filtered.append(s)
    before = ''.join(filtered)
    filtered.reverse()
    after = ''.join(filtered)
    return before == after

print(solution('기러기'))