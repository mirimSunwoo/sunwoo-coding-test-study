function solution(phone_number) {
    front_number = phone_number.slice(0,-4);
    back_number = phone_number.slice(-4);
    return '*'.repeat(front_number.length)+back_number;
}

//정규식 풀이
function hide_numbers(s) {
  return s.replace(/\d(?=\d{4})/g, "*");
}