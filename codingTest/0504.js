//테스트 케이스 2개 성공 1개 실패
function arr_min(arr){
    var sort_arr = arr.sort();
    min = sort_arr[0];
    console.log(min);
    return min;
}
function solution(arr) {
    answer = [];
    arr_min(arr);
    for(var i=0; i<arr.length; i++){
        if(arr[i] != min){
            answer.push(arr[i]);
        }else if(arr.length == 1){
            answer.push(-1);
        }
    }
    return answer;
}
//다른사람의 풀이
function solution(arr) {
    var min = arr[0];
    for(var i = 1; i < arr.length; i++) {
        if(min > arr[i]) min = arr[i];
    }
    arr.splice(arr.indexOf(min), 1);
    if(arr.length) return arr;
    else return [-1];
}