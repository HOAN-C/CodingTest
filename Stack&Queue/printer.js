function solution(priorities, location) {
    var count = 0;
    let tmp = 0;
    while(priorities.length) {
        max = Math.max(...priorities);
        if(priorities[0] == max) {
            tmp = priorities.shift();
            count ++;
            location --;
            if(location == -1) {
                return count;
            }
        } else {
            tmp = priorities.shift();
            priorities.push(tmp);
            location --;
            if(location == -1) {
                location = priorities.length - 1;
            }
        }
    }
}