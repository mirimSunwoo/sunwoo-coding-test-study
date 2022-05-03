function solution(n) {
    for(var x = 0; x <= n; x++){
        if(n%x == 1 && x != 1){
            return x
        }
    }
}
//while문으로 푼 다른사람의 풀이
function solution(n, x = 1) {
    while (x++) {
        if (n % x === 1) {
            return x;
        }
    }
}