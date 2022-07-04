function solution(progresses, speeds) {
    let index = 0; //큐 왼쪽 부분 표시
    let answer = [];
    while (true) {
        let count = 0; //배포되는 기능 수
        for(let i=0; i<progresses.length; i++) {
            progresses[i] += speeds[i];
        }
        for(let i=index; i<progresses.length; i++) {
            if (progresses[index]>=100) {
                count++;
                index++;
            }
        }
        if(count != 0){
            answer.push(count);
        }
        if(index == progresses.length) {
            return answer;
        }
    }
}