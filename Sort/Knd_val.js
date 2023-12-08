// [1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]
function solution(array, commands) {
    let answer = [];
    let tmp = [];
    for(let i=0; i<commands.length; i++) {
        for(let j=commands[i][0]-1; j<commands[i][1]; j++) {
            tmp = array.slice(commands[i][0]-1, commands[i][1]);
            tmp.sort(function(a, b) {
                return a-b;
            })
        }
        answer.push(tmp[commands[i][2]-1]);
        tmp = [];
    }
    return answer;
}

console.log(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))