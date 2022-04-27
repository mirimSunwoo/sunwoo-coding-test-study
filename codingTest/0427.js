function solution(seoul) {
    var answer = String(seoul.findIndex(v=>v=="Kim")); //callback함수를 써야한다.
    return "김서방은 "+answer +"에 있다"
}

//다른사람의 풀이
function findKim(seoul){
  var idx = seoul.indexOf('Kim'); //callback함수를안써도 되는 편리함이 있다
  return "김서방은 " + idx + "에 있다";
}
//indexOf함수 : 문자열에서 특정 문자열을 찾고, 검색된 문자열이 첫번째로 나타나는 index를 리턴한다
//find : 판별 함수를 ㅁ나족하는 첫 요소를 반환(callback함수 필요)
//findIndex : 판별 함수를 만족하는 첫 식별자 반환(//)