//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/41219061a10a4994b65d6191d96e4968

import java.util.*;
import java.io.*;

public class Main {
    static int dp[] = new int[12];
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;
        for(int i = 4;i <= 11;i++) 
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
        
        int T = rd.nextInt();
        while(T --> 0) {
            int n = rd.nextInt();
            System.out.println(dp[n]);
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
