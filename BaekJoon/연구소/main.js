//입력
// 7 7
// 2 0 0 0 1 1 0 //0, 0
// 0 0 1 0 1 2 0 //1, 5
// 0 1 1 0 1 0 0
// 0 1 0 0 0 0 0
// 0 0 0 0 0 1 1
// 0 1 0 0 0 0 0
// 0 1 0 0 0 0 0

//출력
//27

//입력
// 8 8
// 2 0 0 0 0 0 0 2
// 2 0 0 0 0 0 0 2
// 2 0 0 0 0 0 0 2
// 2 0 0 0 0 0 0 2
// 2 0 0 0 0 0 0 2
// 0 0 0 0 0 0 0 0
// 0 0 0 0 0 0 0 0
// 0 0 0 0 0 0 0 0

//출력

// while (true) {
//   console.log("Enter the size");
// }

/** 입력: 맵 배열 입력 / 출력: 맵 배열 */
function print(arr) {
  for (var i = 0; i < arr.length; i++) {
    console.log(arr[i]);
  }
}

/** 입력: 지도 배열 / 출력: 바이러스 위치(좌표) 배열 */
function virusPositionCheck(arr) {
  var result = [];
  for (var i = 0; i < arr.length; i++) {
    if (arr[i].indexOf(2) != -1) {
      result.push([i, arr[i].indexOf(2)]);
    }
  }
  return result;
}

/** 입력: 바이러스 좌표배열, 맵 배열 / 출력: 바이러스 예상경로 확인된 맵 배열 */
function virusWayCheck(arr, map) {
  var x = map[0].length;
  var y = map.length;
}

var size = [7, 7];
var map = [
  [2, 0, 0, 0, 1, 1, 0],
  [0, 0, 1, 0, 1, 2, 0],
  [0, 1, 1, 0, 1, 0, 0],
  [0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 1],
  [0, 1, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 0, 0],
];

var virusPosition = virusPositionCheck(map);

for (var i = virusPosition.length; i >= 1; i--) {
  targetPosition = virusPosition.pop();
}
