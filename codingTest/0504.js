function solution(arr) {
    min = 0;
    var answer = [];
    for(var i=0; i<arr.length; i++){
        if(min<arr[i]){
            min = arr[i];
        }
    }
    arr.pop();
    if(arr.length==0){
        arr.push(-1);
        return arr;
    }
    return arr;
}