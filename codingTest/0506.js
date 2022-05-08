function solution(n){
    str_n = String(n);
    sum_n = 0;
    for(var i=0; i<str_n.length; i++){
        sum_n += Number(str_n.substr(i,1));
    }
    return sum_n;
}
//다른사람의 풀이
function solution(n){
    // 문자 풀이
    // return (n+"").split("").reduce((acc, curr) => acc + parseInt(curr), 0)
    // 숫자풀이
    var sum = 0;
    do {
        sum += n%10;
        n = Math.floor(n/10);
    } while(n > 0);

    return sum;
}