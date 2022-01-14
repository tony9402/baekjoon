//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/c9652354fc7a49abb8ab83b3ef99f75d

import java.util.*;
import java.io.*;

public class Main {
    static boolean valid[] = new boolean[10];
    static int ans = Integer.MAX_VALUE;
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        
        // 고장난 번호를 입력받아 배열에서 false로 설정
        Arrays.fill(valid, true);
        int N = rd.nextInt();
        int M = rd.nextInt();
        for(int i = 0;i < M;i++) {
            int m = rd.nextInt();
            valid[m] = false;
        }
        
        // 가장 가까운 번호로 이동하여 +,-로 도착번호로 가는 경우
        // 이동할 수 있는 모든 번호에 대해 검사한다 
        for(int i = 0;i <= 999999;i++) {
            String num = Integer.toString(i);
            int len = num.length();
            boolean isbroken = false;
            // 이동할 번호 i로 이동 가능한지 확인
            // 하나의 숫자라도 고장나 있으면 이동 불가
            for(int j = 0;j < len;j++) {
                if(valid[num.charAt(j) - '0'] == false) {
                    isbroken = true;
                    break;
                }
            }
            
            // 이동 가능한 경우
            // 이동할 때 누른 번호 수(len) + 도착번호와의 차이
            if(isbroken == false) {
                int dif = Math.abs(i - N) + len;
                ans = Math.min(ans, dif);
            }
        }
        
        // +,-버튼만을 이용하여 도착번호로 가는 경우
        // 도착위치(N) - 시작위치(100)
        int dif = Math.abs(N - 100);
        ans = Math.min(ans, dif);
        
        System.out.println(ans);
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
