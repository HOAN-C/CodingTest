// [6, 10, 2]	"6210"

// [3, 30, 34, 5, 9]	"9534330"

function solution(numbers) {
    let tmp = [];
    tmp = numbers.map(number => number.toString()).sort((a, b) => (b+a)-(a+b));
    if(tmp[0] == 0) {
        return "0";
    }
    return String(tmp.join(''));
}

console.log(solution([3, 30, 34, 5, 9]));
console.log(solution([6, 10, 2]));