function solution(n) {
    var answer = [];
    var StrN = String(n)
    for(var i=0; i<StrN.length; i++){
        answer.push(n%10);
        console.log(n%10);
        n = parseInt(n/10);
    }
    return answer;
}
//다른사람 풀이
function solution(n) {
    // 문제풀이_1
    return (n+"").split("").reverse().map(v => parseInt(v));
    // 문제풀이_2
    var arr = [];
    do {
        arr.push(n%10);
        n = Math.floor(n/10);
    } while (n>0);
    return arr;
}