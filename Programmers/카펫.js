function solution(brown, yellow) {
  let maxWidth = (brown - 2) / 2;
  let width = maxWidth;
  let height = 3;
  for (height; height < maxWidth; height++) {
    console.log(width, height);
    if ((width - 2) * (height - 2) == yellow) {
      console.log(width, height);
      break;
    }
    width--;
  }

  let answer = [width, height];
  return answer;
}

console.log(solution(24, 24));
