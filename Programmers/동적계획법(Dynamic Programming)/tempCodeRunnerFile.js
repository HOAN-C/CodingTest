let triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]];

function findMax(triangle, i = 0, j = 0) {
  if (triangle.length - 1 === i) {
    return triangle[i][j];
  }
  let result =
    Math.max(findMax(i + 1, j), findMax(i + 1, j + 1)) + triangle[i][j];
  return result;
}

console.log(findMax(triangle));
