'''
파일 업로드를 위한 파일 전보를 확인하는 함수의 빈칸 채우기
'''
def solution(file_info):
    sucess = 0
    fail = 0
    for f in file_info:
        splited = f.split(",")
        if splited[0] == "jpeg" and int(splited[2]) < 1000:
            sucess +=1
        else:
            fail += 1
        return sucess,fail

print(solution(["jpeg,all.jpg,500","mpeg,all.mp3,500"]))