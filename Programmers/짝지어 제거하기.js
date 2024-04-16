function solution(s) {
  let stack = [];

  for (let char of s) {
    if (stack.length > 0 && stack[stack.length - 1] === char) {
      stack.pop(); // 마지막 문자와 현재 문자가 같다면 제거
    } else {
      stack.push(char); // 다르면 스택에 추가
    }
  }

  return stack.length === 0 ? 1 : 0;
}

let s = "baabaa";
console.log(solution(s));
