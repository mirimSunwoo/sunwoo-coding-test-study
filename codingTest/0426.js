function a(num){
    var cnt = 0;
    for(var i=1; i<=num; i++){
        if(num%i == 0){
            cnt += 1;
        }
    }
    return cnt
}
function solution(left, right) {
    var answer = 0;
    for(var x = left; x<=right; x++){
        if(a(x)%2==0){
            answer += x;
        }else{
            answer -= x;
        }

    }
    return answer;
}