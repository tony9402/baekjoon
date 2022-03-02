//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/e4ac08ca21d54fa5bdfa599c5359a0b4

import java.util.*;
import java.io.*;

public class Main {
    static int dp[];
    static int arr[];
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        
        int N = rd.nextInt();
        // dp[i]는 1 ~ i까지 'i번째 숫자를 포함한' 최장길이
        dp = new int[N + 10];
        arr = new int[N + 10];
        
        // 배열을 입력 받음과 동시에 dp값을 전부 1로 초기화 합니다.
        // 항상 길이는 최소 1 이상이기 때문
        for(int i = 1;i <= N;i++) {
            arr[i] = rd.nextInt();
            dp[i] = 1;
        }
        
        // 1 ~ (i - 1) 까지 숫자를 살피는데 arr[i]보다 작고
        // dp[i] < dp[j] + 1 이라면 dp[i]값을 갱신합니다.
        for(int i = 2;i <= N;i++) {
            for(int j = 1;j < i;j++) {
                if(arr[i] > arr[j] && dp[i] < dp[j] + 1)
                    dp[i] = dp[j] + 1;
            }
        }
        
        // dp배열을 돌며 최대값을 찾아 출력합니다.
        int max = 0;
        for(int i = 1;i <= N;i++) 
            max = Math.max(max, dp[i]);
        
        System.out.println(max);
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
