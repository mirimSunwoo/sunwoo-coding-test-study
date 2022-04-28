//나는 파이썬으로 주로 풀었기 때문에 무조건 함수를 써서 풀려고 했다
//하지만 함수를 모르는 사람들은 for문을 사용해서 푸는 모습을 볼 수 있었다
function solution(s) {
    return parseInt(s);
}
//다른 사람의 풀이_1
function strToInt(str){
  return str/1
}
/* -> 댓글반응
= 와 동적언어의 핵심을 찌르네요
= 아.. 항상 이거 보면 자괴감
= 사칙연산 되면서 문자가 자동으로 파싱이 되는거였군요. 잘배우고 갑니다
 */

//다른사람의 풀이_2
function strToInt(str){
  return  +str;
}
/* -> 댓글반응
= 역시 자바스크립트의 세계란...
= int to string => ""+int
= 이게 되는구나 ㅋㅋㅋ
 */
