//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/d70329d0bfa74ad692b57abcff5fc0b3

import java.util.*;
import java.io.*;

class Point {
    int x, y;
    Point(int x, int y){
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static int N, M, T;
    static int[][] castle, distance;
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};
    static boolean[][] visited;
    static Point sword;

    public static void main(String[] args) {
        FastReader rd = new FastReader();

        N = rd.nextInt();
        M = rd.nextInt();
        T = rd.nextInt();

        castle = new int[N + 10][M + 10];
        distance = new int[N + 10][M + 10];
        visited = new boolean[N + 10][M + 10];

        for(int i = 1;i <= N;i++) {
            for(int j = 1;j <= M;j++) {
                castle[i][j] = rd.nextInt();
                if(castle[i][j] == 2)
                    sword = new Point(i, j);
            }
        }

        // bfs로 각 지점까지 거리를 구해놓는다.
        bfs();

        int use_sword = Integer.MAX_VALUE, not_use_sword = Integer.MAX_VALUE;

        // 검을 사용했을 때 걸리는 시간. 구하지 못하는 경우는 int형 최대값
        if(distance[sword.x][sword.y] != 0)
            use_sword = distance[sword.x][sword.y] + (N - sword.x) + (M - sword.y);

        // 검을 사용하지 않고 걸리는 시간. 구하지 못하는 경우는 int형 최대값
        if(distance[N][M] != 0)
            not_use_sword = distance[N][M];

        // 둘 중 작은 값을 T보다 작을때만 출력, 그 외는 Fail출력
        if(Math.min(use_sword, not_use_sword) > T)
            System.out.println("Fail");
        else System.out.println(Math.min(use_sword, not_use_sword));
    }

    static void bfs() {
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(1, 1));
        visited[1][1] = true;

        while(!q.isEmpty()) {
            Point cur = q.poll();

            for(int i = 0;i < 4;i++) {
                int nextx = cur.x + dx[i];
                int nexty = cur.y + dy[i];

                if(nextx <= 0 || nexty <= 0 || nextx > N || nexty > M) continue;
                if(visited[nextx][nexty] == true || castle[nextx][nexty] == 1) continue;

                q.add(new Point(nextx, nexty));
                visited[nextx][nexty] = true;
                distance[nextx][nexty] = distance[cur.x][cur.y] + 1;
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
