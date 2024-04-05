function solution(n) {
  let NbianryCount = 0;
  let Nbinary = n.toString(2); //n 2진수로 변환
  for (i = 0; i < Nbinary.length; i++) {
    //2진수 n 1 갯수 카운트
    if (Nbinary[i] == 1) {
      NbianryCount++;
    }
  }

  for (i = n + 1; true; i++) {
    let IbianryCount = 0;
    let Ibinary = i.toString(2); //i 2진수로 변환
    for (j = 0; j < Ibinary.length; j++) {
      if (Ibinary[j] == 1) {
        IbianryCount++;
      }
    }
    if (IbianryCount == NbianryCount) {
      return i;
    }
  }
}

console.log(solution(15));
