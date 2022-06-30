// Authored by : highjoon
// Co-authored by : -
// Link : http://boj.kr/dfbb944e04d3425b92c43bc40e9d5446

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

function solution(input) {
    let N = Number(input[0]);
    input = input.slice(1).map((v) => v.split(" ").map(Number));
    let board = Array.from({ length: N }, () => Array(N).fill(0));
    const dx = [1, 0, -1, 0];
    const dy = [0, 1, 0, -1];
    let favorites = {};
    let students = [];
    let answer = 0;

    for (let x of input) {
        students.push(x[0]);
        favorites[x[0]] = x.slice(1);
    }

    for (let student of students) {
        let candidates = {};
        for (let row = 0; row < N; row++) {
            for (let col = 0; col < N; col++) {
                if (board[row][col] !== 0) continue;
                let count = [0, 0]; // 우선 순위 수, 비어있는 칸 수,
                for (let i = 0; i < dx.length; i++) {
                    const [nRow, nCol] = [row + dx[i], col + dy[i]];
                    if (nRow < 0 || nRow >= N || nCol < 0 || nCol >= N) continue;
                    if (favorites[student].includes(board[nRow][nCol])) count[0]++;
                    if (!board[nRow][nCol]) count[1]++;
                }
                const key = JSON.stringify(count);
                if (!candidates[key]) candidates[key] = [[row, col]];
                else candidates[key].push([row, col]);
            }
        }
        const sorted = Object.keys(candidates).sort((a, b) => {
            const [a0, a1] = JSON.parse(a);
            const [b0, b1] = JSON.parse(b);
            if (a0 !== b0) return b0 - a0;
            return b1 - a1;
        });
        const [newRow, newCol] = candidates[sorted[0]][0];
        board[newRow][newCol] = student;
    }

    for (let student of students) {
        let favCount = 0;
        for (let row = 0; row < N; row++) {
            for (let col = 0; col < N; col++) {
                if (board[row][col] === student) {
                    for (let i = 0; i < dx.length; i++) {
                        const [nRow, nCol] = [row + dx[i], col + dy[i]];
                        if (nRow < 0 || nRow >= N || nCol < 0 || nCol >= N) continue;
                        if (favorites[student].includes(board[nRow][nCol])) favCount++;
                    }
                }
            }
        }
        switch (favCount) {
            case 0:
                answer += 0;
                break;
            case 1:
                answer += 1;
                break;
            case 2:
                answer += 10;
                break;
            case 3:
                answer += 100;
                break;
            case 4:
                answer += 1000;
                break;
        }
    }

    return answer;
}

console.log(solution(input));
