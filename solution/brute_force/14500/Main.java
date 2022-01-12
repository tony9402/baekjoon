//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/5b16d12ed3924b5da3c52a2f4a03c4f1

import java.util.*;
import java.io.*;

class Pair {
    int x, y;
    Pair(int y, int x){
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static int N, M, max;
    static int paper[][];
    static boolean visited[][];
    static int dx[] = {1, -1, 0, 0};
    static int dy[] = {0, 0, 1, -1};
    public static void main(String[] args) {
        FastReader rd = new FastReader();

        N = rd.nextInt();
        M = rd.nextInt();
        
        paper = new int[N + 10][M + 10];
        visited = new boolean[N + 10][M + 10];
        for(int i = 1;i <= N;i++) {
            for(int j = 1;j <= M;j++) 
                paper[i][j] = rd.nextInt();
        }
        
        // ㅜ모양을 제외한 나머지 모양은 어떻게 회전하던, 대칭하던
        // dfs로 찾을 수 있습니다.
        // 따라서 ㅜ모양만 따로 처리하고 나머지는 dfs로 모든 경우를 찾습니다
        for(int i = 1;i <= N;i++) {
            for(int j = 1;j <= M;j++) {
                dfs(new Pair(i, j), 1, paper[i][j]);
                case_Woo(new Pair(i, j));
            }
        }
        System.out.println(max);
    }
    
    static void case_Woo(Pair cur) {
        int case_1[][] = {{0, 1}, {0, 2}, {1, 1}};  // case 'ㅜ' 
        int case_2[][] = {{0, 1}, {0, 2}, {-1, 1}}; // case 'ㅗ'
        int case_3[][] = {{1, 0}, {2, 0}, {1, 1}};  // case 'ㅏ'
        int case_4[][] = {{1, 0}, {2, 0}, {1, -1}}; // case 'ㅓ'
        
        // ㅜ 모양 확인
        int sum = paper[cur.y][cur.x];
        for(int i = 0;i < 3;i++) {
            int nextx = cur.x + case_1[i][1];
            int nexty = cur.y + case_1[i][0];
                
            if(nextx < 1 || nexty < 1) continue;
            if(nextx > M || nexty > N) continue;
                
            sum += paper[nexty][nextx];
        }
        max = Math.max(sum, max);
        
        // ㅗ 모양 확인
        sum = paper[cur.y][cur.x];
        for(int i = 0;i < 3;i++) {
            int nextx = cur.x + case_2[i][1];
            int nexty = cur.y + case_2[i][0];
                
            if(nextx < 1 || nexty < 1) continue;
            if(nextx > M || nexty > N) continue;
                
            sum += paper[nexty][nextx];
        }
        max = Math.max(sum, max);
        
        // ㅏ 모양 확인
        sum = paper[cur.y][cur.x];
        for(int i = 0;i < 3;i++) {
            int nextx = cur.x + case_3[i][1];
            int nexty = cur.y + case_3[i][0];
                
            if(nextx < 1 || nexty < 1) continue;
            if(nextx > M || nexty > N) continue;
                
            sum += paper[nexty][nextx];
        }
        max = Math.max(sum, max);
        
        // ㅓ 모양 확인
        sum = paper[cur.y][cur.x];
        for(int i = 0;i < 3;i++) {
            int nextx = cur.x + case_4[i][1];
            int nexty = cur.y + case_4[i][0];
                
            if(nextx < 1 || nexty < 1) continue;
            if(nextx > M || nexty > N) continue;
                
            sum += paper[nexty][nextx];
        }
        max = Math.max(sum, max);
    }
    
    static void dfs(Pair cur, int depth, int sum) {
        visited[cur.y][cur.x] = true;
        // 깊이가 4이면 max값을 갱신하고 리턴합니다.
        if(depth == 4) {
            max = Math.max(max, sum);
            return;
        }
        // 4방향으로 이동해가며 만들 수 있는 모든 모양의 경우를 확인합니다
        // 어떠한 모양이던 만들 수 있습니다
        for(int i = 0;i < 4;i++) {
            int nextx = cur.x + dx[i];
            int nexty = cur.y + dy[i];
            
            if(nextx < 1 || nexty < 1) continue;
            if(nextx > M || nexty > N) continue;
            if(visited[nexty][nextx]) continue;

            dfs(new Pair(nexty, nextx), depth + 1, sum + paper[nexty][nextx]);
            visited[nexty][nextx] = false;
        }
        visited[cur.y][cur.x] = false;
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
