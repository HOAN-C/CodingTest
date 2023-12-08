function solution(n, computers) {
    let answer = n;
    for(let i=0; i<computers.length; i++) {
        for(let j=i+1; j<computers.length; j++) {
            console.log(i, j, " : ", computers[i][j]);
        }
    }
    return answer;
}

console.log(solution(3, [[1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1]]));