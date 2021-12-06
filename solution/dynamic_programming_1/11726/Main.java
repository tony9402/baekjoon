//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/54a281a936484bbda48800ca4f5f546c

/*
문제는 1x2 2x1 이라고 주어졌지만 사실은 2x1타일을 쓰는 순간
밑에도 2x1타일을 써야하기 때문에 2x2타일이라고 생각해도 무방합니다.
따라서 dp[i] = dp[i] = dp[i - 1] + dp[i - 2] 입니다.
현재 타일 경우 = (이전에) 1x2타일을 썼을 때 + 2x2타일을 썼을 때  
*/

import java.util.*;
import java.io.*;

public class Main {
    static int[] dp = new int[1010]; 

    public static void main(String[] args) {
        FastReader rd = new FastReader();

        int n = rd.nextInt();

        dp[1] = 1;
        dp[2] = 2;

        // dp[i] = dp[i - 1] + dp[i - 2]
        for(int i = 3;i <= n;i++) 
            dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;
        System.out.println(dp[n]);
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
