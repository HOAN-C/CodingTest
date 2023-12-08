function solution(jobs) {
    let time = 0;   //시간 나타내는 변수
    let jobEndTime = 0;     //현재 작업이 끝날 시간
    let fastestInsert = 0;      //가장 최근에 들어온 시간표시
    let ans = [];

    while(jobs.length) {
        if(jobEndTime == time) { //현재 작업이 없으면 다음 작업 탐색
            for(let i=0; i<jobs.length; i++) {
                if(jobs[i][0]<=jobEndTime){

                }
            }
        }

        time++;
    }

    return 0;
}


console.log(solution([[0, 3], [1, 9], [2, 6]]));