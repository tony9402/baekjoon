//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/b8fc50e235a44c1a9cfd95e860c9f8be

import java.util.*;
import java.io.*;

class Point {
    int y, x;
    Point(int y, int x) {
        this.y = y;
        this.x = x;
    }
}

public class Main {
    static char[][] chess;
    static boolean[][] visited;
    static int wall_count = 0;
    static int[] dx = {1, 0, -1, 0, 1, -1, 1, -1, 0};
    static int[] dy = {0, 1, 0, -1, -1, 1, 1, -1, 0};

    public static void main(String[] args) {
        FastReader rd = new FastReader();

        chess = new char[10][10];
        visited = new boolean[10][10];

        // 입력을 받으면서 벽 개수를 구함
        for(int i = 1;i <= 8;i++) {
            String str = rd.nextLine();
            for(int j = 1;j <= 8;j++) {
                chess[i][j] = str.charAt(j - 1);
                if(chess[i][j] == '#') wall_count++;
            }
        }

        if(bfs() == true) System.out.println("1");
        else System.out.println("0");
    }

    static boolean bfs() {
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(8, 1));

        while(!q.isEmpty()) {
            int check = q.size();

            // 현재위치에서 다음 위치로 갈 수 있는 곳을 큐에 집어 넣고
            // 다음 while roop때 큐안의 모든 값들을 검사한 후에 벽을 움직여야 한다.
            // 그렇지 않으면 벽만 계속 이동하는 상황이 벌어진다.
            for(int i = 0;i < check;i++) {
                Point cur = q.poll();
                // 현재 위치가 벽과 같은 위치(즉 벽에 깔린 상황)라면 넘어간다.
                if(chess[cur.y][cur.x] == '#') continue;

                // 도착점 이거나 또는 벽이 없어서 반드시 도착점에 도달할 수 있는 상황.
                if(cur.y == 1 && cur.x == 8 || wall_count == 0) return true;

                // 8방향 + 제자리 위치까지 총 9방향을 검사하여 큐에 넣는다.
                for(int j = 0;j < 9;j++) {
                    int nexty = cur.y + dy[j];
                    int nextx = cur.x + dx[j];	

                    if(nextx <= 0 || nexty <= 0 || nextx > 8 || nexty > 8) continue;
                    if(visited[nexty][nextx] == true || chess[nexty][nextx] == '#') continue;

                    visited[nexty][nextx] = true;
                    q.add(new Point(nexty, nextx));
                }
            }

            // 이동하였다가 다시 되돌아 올 수 있기 때문에 초기화.
            for(int i = 0;i < 10;i++)
                Arrays.fill(visited[i], false);

            // 벽이 남아있을 때 벽을 옮긴다.
            if(wall_count > 0) moveWall();
        }
        return false;
    }

    static void moveWall() {
        for(int i = 8;i > 0;i--) {
            for(int j = 1;j <= 8;j++) {
                if(chess[i][j] != '#') continue;

                int nextwall = i + 1;
                if(nextwall <= 8) {
                    chess[nextwall][j] = '#';
                    chess[i][j] = '.';
                }
                else {
                    chess[i][j] = '.';
                    wall_count--;
                }
            }
        }
    }

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
