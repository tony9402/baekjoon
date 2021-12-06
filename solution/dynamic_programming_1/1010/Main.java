//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/00ddd7d473554b639c5e65eb1e1d8269

import java.util.*;
import java.io.*;

public class Main {
    static int[][] dp = new int[30][30]; 

    public static void main(String[] args) {
        FastReader rd = new FastReader();

        int T = rd.nextInt();

        // 조합공식을 이용하여 풀이가능 (M C N)
        dp[0][0] = 1;
        for(int j = 1;j < 30;j++) {
            dp[j][0] = 1;
            for(int k = 1;k <= j;k++) 
                dp[j][k] = dp[j - 1][k - 1] + dp[j - 1][k];
        }

        for(int i = 0;i < T;i++) {
            int N = rd.nextInt();
            int M = rd.nextInt();

            System.out.println(dp[M][N]);
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
