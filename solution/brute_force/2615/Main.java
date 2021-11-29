// Authored by : smw123123
// Co-authored by : -
// Link : http://boj.kr/7fe90aad8ed1484f95674d7fd4464d5c

import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    static int[][] board;
    static int lastX, lastY;
    public static void main(String[] args) {
        FastReader sc = new FastReader();
        board = new int[19][19];
        for (int i = 0; i < 19; i++) {
            for (int j = 0; j < 19; j++) {
                board[i][j] = sc.nextInt();
            }
        }
        for (int i = 0; i < 19; i++) {
            for (int j = 0; j < 19; j++) {
                int cur = board[i][j];
                if(cur > 0) {
                    for (int d = 0; d < 4; d++) {
                        int nx = i + dx[d];
                        int ny = j + dy[d];
                        if(!isPossible(nx, ny)) continue;
                        if(board[nx][ny] == cur) {
                            var a = checkFirst(nx, ny, cur, d) + 1;
                            if(a == 5) {
                                var b = checkSecond(cur, d);
                                if(a == b) {
                                    System.out.println(cur);
                                    System.out.println((lastX+ dx[d]+1) + " " + (lastY+dy[d]+1));
                                    return;
                                }
                            }
                        }
                    }
                }
            }
        }
        System.out.println(0);
    }

    private static int checkFirst(int x, int y, int cur, int direction) {
        lastX = x;
        lastY = y;
        int nx = x + dx[direction];
        int ny = y + dy[direction];
        if(!isPossible(nx, ny)) return 1;
        if(board[nx][ny] == cur) {
            return checkFirst(nx, ny, cur, direction) + 1;
        }
        else
            return 1;
    }

    private static int checkSecond(int cur, int d) {
        lastX = lastX + rdx[d];
        lastY = lastY + rdy[d];
        if(!isPossible(lastX, lastY)) return 1;
        if(board[lastX][lastY] == cur) {
            return checkSecond(cur, d) + 1;
        }
        else {
            return 1;
        }
    }
    private static boolean isPossible(int x, int y) {
        return x >= 0 && x < 19 && y >= 0 && y < 19;
    }

    // 오른쪽 위↗, 오른쪽→, 오른쪽 아래↘, 아래↓
    static int[] dx = {-1, 0, 1, 1};
    static int[] dy = {1, 1, 1, 0};

    // 왼쪽 아래↙, 왼쪽←, 왼쪽 위↖, 위↑
    static int[] rdx = {1, 0, -1, -1};
    static int[] rdy = {-1, -1, -1, 0};


    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while(st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                }
                catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() { return Integer.parseInt(next()); }
        long nextLong() { return Long.parseLong(next()); }
        double nextDouble() { return Double.parseDouble(next()); }
        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            }
            catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}
