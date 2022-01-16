//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/c52a0cc52576401a9cbe5f8cab4d2c9a

import java.util.*;
import java.io.*;

public class Main {
    static int place[][];
    static int dx[] = {0, 1, 0, -1}; // 북, 동, 남, 서 
    static int dy[] = {-1, 0, 1, 0};
    static int N, M, r, c, d, ans = 1;
    public static void main(String[] args) {
        FastReader rd = new FastReader();

        N = rd.nextInt();
        M = rd.nextInt();
        r = rd.nextInt();
        c = rd.nextInt();
        d = rd.nextInt();
        place = new int[N + 10][M + 10];
        for(int i = 0;i < N;i++) {
            for(int j = 0;j < M;j++) 
                place[i][j] = rd.nextInt();
        }

        dfs(r, c, d);
        System.out.println(ans);
    }

    static void dfs(int y, int x, int d) {
        // 청소가 된 구역은 -1로 한다.
        place[y][x] = -1;
        
        // 4방향을 살피며 청소할 수 있으면 이동한다
        for(int i = 0;i < 4;i++) {
            d = (d + 3) % 4;
            int nx = x + dx[d];
            int ny = y + dy[d];
            if(nx >= 0 && ny >= 0 && nx < M && ny < N && place[ny][nx] == 0) {
                ans++;
                dfs(ny, nx, d);
                // 복귀할 때 다른곳은 가지 않도록 리턴해준다
                return;
            }
        }
        
        // 네 방향 모두 청소가 되어 있거나 벽인 경우
        // 뒤로 갈 수 있으면 방향을 유지한 채 뒤로 이동한다
        int b = (d + 2) % 4;
        int bx = x + dx[b];
        int by = y + dy[b];
        if(bx >= 0 && by >= 0 && bx < M && by < N && place[by][bx] != 1)
            dfs(by, bx, d);
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
        long nextLong() { return Long.parseLong(next()); }
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
