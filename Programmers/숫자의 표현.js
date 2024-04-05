function solution(n) {
  let answer = 0;
  for (i = 1; i <= n; i++) {
    console.log("----------");
    let sum = 0;
    for (j = i; j <= n; j++) {
      sum += j;
      console.log(j);
      if (sum == n) {
        console.log("Found!!");
        answer++;
        break;
      }
    }
  }
  return answer;
}

console.log(solution(10000));
