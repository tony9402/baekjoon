//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/65f7daf6f417474483f6ae1f03b9591c

import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static String ans = "";
    public static void main(String[] args) {
        FastReader rd = new FastReader();

        N = rd.nextInt();

        dfs(0); 
    }
    
    // dfs로 소수일 때 자리수를 늘려가며 진행한다
    static void dfs(int length) {
        if(length == N) {
            System.out.println(ans);
        }
        
        for(int i = 0;i <= 9;i++) {
            String nnum = ans + (char)(i + '0');
            if(isPrime(nnum) == true) {
                ans = nnum;
                dfs(length + 1);
                ans = ans.substring(0, ans.length() - 1);
            }
        }
    }
    
    // 소수 판별 함수
    // num의 제곱근까지 확인하여 소수를 판별한다
    static boolean isPrime(String num) {
        int n = Integer.parseInt(num);
        if(n == 1 || n == 0) return false;
        for(int i = 2;i * i <= n;i++)
            if(n % i == 0) return false;
        return true;
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
