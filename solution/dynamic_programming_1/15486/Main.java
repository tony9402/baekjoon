// Authored by : smw123123
// Co-authored by : -
// Link : http://boj.kr/a9b5c6f0b2a443549ae67563af0f5e55

import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {

        FastReader rd = new FastReader();
        int N = rd.nextInt();
        int[] dp = new int[N+1];
        int T, P;

        for(int i = 0; i < N; i++) {
            T = rd.nextInt();
            P = rd.nextInt();
            dp[i+1] = Math.max(dp[i], dp[i+1]);
            if(i + T <= N) {
                dp[i+T] = Math.max(dp[i+T], dp[i] + P);
            }
        }
        System.out.println(dp[N]);
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

// 설명 링크 : https://github.com/tony9402/baekjoon/pull/249#issue-978163457
