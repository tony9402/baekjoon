//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/342101ba2b5246bb9801f2d356ea8c56

import java.util.*;
import java.io.*;
import java.math.*;

public class Main {
    static BigInteger[][] dp = new BigInteger[110][110]; 

    public static void main(String[] args) {
        FastReader rd = new FastReader();

        int n = rd.nextInt();
        int m = rd.nextInt();

        // 매우매우 큰수가 나오는 조합(n C m), 따라서 biginteger사용
        dp[0][0] = new BigInteger("1");

        for(int i = 1;i <= n;i++) {
            dp[i][0] = new BigInteger("1");
            for(int j = 1;j <= i;j++) {
                // biginteger는 string이라서 null로 초기화 되어 있기 때문에
                // 각 예외상황마다 값을 정해주어야 한다. 
                if(i == j) dp[i][j] = new BigInteger("1");
                else if(i < j) dp[i][j] = new BigInteger("0");		 
                else dp[i][j] = dp[i - 1][j - 1].add(dp[i - 1][j]);	
            }
        }

        System.out.println(dp[n][m]);
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
