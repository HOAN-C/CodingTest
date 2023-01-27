// 세로 N, 가로 M 3<= N, M <=50
// r, c 로봇 좌표
// d 로봇 방향 0 북, 1 동, 2 남, 3 서

var N = 11; //가로 11
var M = 10; //세로 10
var botPosition = [7, 4, 0];
var map = [
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
  [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
  [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
  [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
  [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
];
var cleanedCount = 0;

// 0: 공간, 1: 벽, 2: 청소된 공간
//구현해야 되는 기능
//2. 탐색

/**
 * 로봇 현 위치 청소(map 데이터 수정), 청소 카운터 증가
 * @param {} botPosition : 로봇 위치
 * @param {} map : 지도
 * @param {} cleanedCount : 청소 카운터
 */
function clean(botPosition, map, cleanedCount) {
  if (map[botPosition[0]][botPosition[1]] !== 2) {
    map[botPosition[0]][botPosition[1]] = 2; //2: 청소됨
    cleanedCount++; //카운트 증가
  } else {
    console.log("clean func error : already cleanded space");
  }
}

/**
 * 시계 반대방향(왼쪽) 으로 90도 회전
 * @param {*} botPosition : 로봇 위치
 */
function turn(botPosition) {
  botPosition[2] = botPosition[2] - 1;
  if (botPosition[2] == -1) {
    botPosition[2] = 3;
  }
}

/**
 * 바라보고 있는 기준으로 전진 또는 후진한다.
 * @param {*} botPosition : 로봇 위치
 * @param {*} forward : 방향(1 : 전진, -1 : 후진)
 */
function move(botPosition, forward) {
  if (botPosition[2] == 0) {
    botPosition[0] = botPosition[0] + forward;
  } else if (botPosition[2] == 1) {
    botPosition[1] = botPosition[1] + forward;
  } else if (botPosition[2] == 2) {
    botPosition[0] = botPosition[0] + forward;
  } else if (botPosition[2] == 3) {
    botPosition[1] = botPosition[1] + forward;
  }
}
// 1. 현재 위치를 청소한다. clean func
// 2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다. scan func
//      2.1 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
//      2.2 왼쪽 방향에 청소할 공간이 없다면(청소된 공간이 있다면?), 왼쪽으로 회전하고 2번으로 돌아간다.
//      2.3 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
//      2.4 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.

while (true) {
  clean(botPosition, map, cleanedCount);
}
