// Authored by : yundosa2
// Co-authored by : -
// Link: http://boj.kr/57673ced91544798ab3cbda0c8cb5525

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

function solution(input) {
  let [N, M] = input[0].split(" ").map(Number);
  let board = input.slice(1, N + 1).map((v) => v.split(" ").map(Number));
  let moves = input.slice(N + 1).map((v) => v.split(" ").map(Number));
  let clouds = [
    [N - 2, 0],
    [N - 2, 1],
    [N - 1, 0],
    [N - 1, 1],
  ];
  const directions = {
    1: [0, -1],
    2: [-1, -1],
    3: [-1, 0],
    4: [-1, 1],
    5: [0, 1],
    6: [1, 1],
    7: [1, 0],
    8: [1, -1],
  };
  const diagX = [-1, -1, 1, 1];
  const diagY = [-1, 1, -1, 1];
  let answer = 0;

  for (let move of moves) {
    // 1번
    const nextClouds = [];
    for (let cloud of clouds) {
      const [row, col] = cloud;
      const direction = directions[move[0]];
      const distance = move[1];
      let nRow = (row + direction[0] * distance) % N;
      let nCol = (col + direction[1] * distance) % N;
      nRow = nRow < 0 ? nRow + N : nRow;
      nCol = nCol < 0 ? nCol + N : nCol;
      nextClouds.push([nRow, nCol]);
    }

    // 2번
    let visited = Array.from({ length: N }, () => Array(N).fill(false));
    for (let cloud of nextClouds) {
      const [row, col] = cloud;
      board[row][col]++;
      visited[row][col] = true;
    }

    // 3번
    clouds = [];

    // 4번
    for (let cloud of nextClouds) {
      const [row, col] = cloud;
      let count = 0;
      for (let i = 0; i < 4; i++) {
        const [nRow, nCol] = [row + diagX[i], col + diagY[i]];
        if (nRow < 0 || nRow >= N || nCol < 0 || nCol >= N || board[nRow][nCol] < 1) continue;
        count++;
      }
      board[row][col] += count;
    }

    // 5번
    for (let row = 0; row < N; row++) {
      for (let col = 0; col < N; col++) {
        if (board[row][col] >= 2 && !visited[row][col]) {
          board[row][col] -= 2;
          clouds.push([row, col]);
        }
      }
    }
  }

  // 최종 계산
  for (let row = 0; row < N; row++) {
    for (let col = 0; col < N; col++) {
      answer += board[row][col];
    }
  }
  return answer;
}

console.log(solution(input));
