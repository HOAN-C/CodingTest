//[3, 0, 6, 1, 5]	3

function solution(citations) {
    citations.sort();
    let answer = 0;
    for(let i=0; i<citations.length; i++) {
        if(citations[i]<=(citations.slice(i)).length) {
            answer = citations[i];
        }
    }
    return answer;
}

console.log(solution([3, 0, 6, 1, 5]));
console.log(solution([1, 2, 3, 4, 5, 4, 4]));
console.log(solution([4, 2, 2, 4, 7, 9, 5, 6, 7, 6, 3, 6, 5, 4]));