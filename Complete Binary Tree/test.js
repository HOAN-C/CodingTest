function solution(answer_list) {
    let first = 0;
    answer = [1, 2, 3, 4, 5];
    for(let i=0; i<answer_list.length; i++) {
        if(answer_list[i] == answer[i%answer.length]) {
            first++;
        }
    }
    let sec = 0;
    answer = [2,1,2,3,2,4,2,5];
    for(let i=0; i<answer_list.length; i++) {
        if(answer_list[i] == answer[i%answer.length]) {
            sec++;
        }
    }
    let third = 0;
    answer = [3,3,1,1,2,2,4,4,5,5];
    for(let i=0; i<answer_list.length; i++) {
        if(answer_list[i] == answer[i%answer.length]) {
            third++;
        }
    }
    let num = [1, 2, 3];
    let total = [first, sec, third];
    let rtn = [];
    let max = Math.max(...total);
    for(let i=0; i<total.length; i++) {
        if(total[i] == max) {
            rtn.push(num[i])
        }
    }
    return rtn;
}