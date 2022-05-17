function add(arr){
    sum = 0;
    for(var i=0; i<arr.length; i++){
         sum += arr[i];
    }
    return sum;
}
function solution(numbers) {
    array = [0,1,2,3,4,5,6,7,8,9]
    answer = add(array)-add(numbers);
    return answer;
}

//다른사람의 풀이
function solution(numbers) {
    return 45 - numbers.reduce((cur, acc) => cur + acc, 0);
}
//배열.reduce((누적값, 현잿값, 인덱스, 요소) => { return 결과 }, 초깃값);