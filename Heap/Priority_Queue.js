// I 숫자	큐에 주어진 숫자를 삽입합니다.
// D 1	큐에서 최댓값을 삭제합니다.
// D -1	큐에서 최솟값을 삭제합니다.

// ["I 16","D 1"]	[0,0]
// ["I 7","I 5","I -5","D -1"]	[7,5]

function solution(operations) {
    let answer = [];
    for(let i=0; i<operations.length; i++) {
        if(operations[i][0] == "I") {
            let tmp = operations[i];
            answer.push(Number(tmp.substring(2, tmp.length)));
            answer.sort(function(a, b) {
                return b - a;
            });
        } else if(operations[i] == "D 1") {
            answer.shift();
        } else if(operations[i] == "D -1") {
            answer.pop();
        }
    }
    if((answer[0] == undefined) && (answer[1] == undefined)) {
        return [0, 0];
    } else if((answer[1] == undefined)) {
        if(answer[0] >= 0) {
            answer.push(0);
        } else {
            answer.unshift(0);
        }
    }
    return [answer[0], answer[answer.length-1]]; 
}