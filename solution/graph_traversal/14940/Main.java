//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/07019ff960d14af3840cf2210023fbf3

import java.util.*;
import java.io.*;

class Pair{
    int x, y;
    Pair(int x, int y){
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static int[][] map, distance;
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int n, m;
    static boolean[][] visited;

    public static void main(String[] args) {
        FastReader rd = new FastReader();

        n = rd.nextInt();
        m = rd.nextInt();

        map = new int[n + 10][m + 10];
        distance = new int[n + 10][m + 10];
        visited = new boolean[n + 10][m + 10];

        // 목표지점 저장
        int destX = 0, destY = 0;
        for(int i = 1;i <= n;i++) {
            for(int j = 1;j <= m;j++) {
                map[i][j] = rd.nextInt(); 

                if(map[i][j] == 2) {
                    destX = i;
                    destY = j;
                }
            }
        }

        // 목표지점을 기준으로 bfs를 진행하여
        // 각 위치별로 얼만큼 떨어져 있는지 구한다.
        bfs(destX, destY);

        // 거리가 0인데 map값이 1이면 갈 수 없는 좌표이다 따라서 -1
        for(int i = 1;i <= n;i++) {
            for(int j = 1;j <= m ;j++) {
                if(distance[i][j] == 0 && map[i][j] == 1)
                    System.out.print("-1 ");
                else 
                    System.out.print(distance[i][j] + " ");
            }
            System.out.print("\n");
        }
    }

    static void bfs(int X, int Y) {
        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(X, Y));
        visited[X][Y] = true;

        while(!q.isEmpty()) {
            Pair cur = q.poll();

            for(int i = 0;i < 4;i++) {
                int nextx = cur.x + dx[i];
                int nexty = cur.y + dy[i];

                if(nextx <= 0 || nexty <= 0 || nextx > n || nexty > m) continue;
                if(visited[nextx][nexty] == true || map[nextx][nexty] == 0) continue;

                q.add(new Pair(nextx, nexty));
                distance[nextx][nexty] = distance[cur.x][cur.y] + 1;
                visited[nextx][nexty] = true;
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
