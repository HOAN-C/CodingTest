function solution(n, words) {
  let answer = [0, 0];
  let when = 0;
  let who = 0;

  for (let i = 1; i < words.length; i++) {
    //Last Of Past
    let LOP = words[i - 1][words[i - 1].length - 1];
    //First Of Now
    let FON = words[i][0];

    answer = [who, when];
    if (LOP != FON) {
      who = (i % n) + 1;
      when = Math.floor(i / n) + 1;
      answer = [who, when];
      break;
    }

    let check = words.slice(0, i);

    if (check.includes(words[i])) {
      who = (i % n) + 1;
      when = Math.floor(i / n) + 1;

      answer = [who, when];
      break;
    }
  }
  return answer;
}

console.log(
  "Solution: " +
    solution(3, [
      "tank",
      "kick",
      "know",
      "wheel",
      "land",
      "dream",
      "mother",
      "robot",
      "tank",
    ])
);
