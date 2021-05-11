// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/f810af85a30044488b4324ded456497d
import java.io.*;
import java.util.*;
import java.lang.*;

public class Main {
    static int [][]map;
    static int N, M;
    static int answer;
    static public void main(String[] args) {
        FastReader rd = new FastReader();

        N = rd.nextInt();
        M = rd.nextInt();

        map = new int[N + 1][M + 1]; // 1-index
        
        dfs(0);

        System.out.println(answer);
    }

    static void dfs(int cnt) {
        if(cnt == N * M) {
            answer ++;
            return ;
        }
        int y = cnt / M + 1;
        int x = cnt % M + 1;
        
        if(map[y - 1][x] == 1 && map[y][x - 1] == 1 && map[y - 1][x - 1] == 1) { // 현재 놓을 수 없는 곳
            dfs(cnt + 1);
        }
        else {
            dfs(cnt + 1); // 선택 안하고 다음껄 볼 경우
            map[y][x] = 1;
            dfs(cnt + 1); // 선택 하고 다음껄 볼 경우
            map[y][x] = 0;
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
