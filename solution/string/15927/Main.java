//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/927b144f383548d79499015d9215444b

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        String st = rd.nextLine();
        
        // 입력값이 팰린드롬이 아니면 정답은 (입력값의 길이)
        for(int i = 0;i < st.length() / 2;i++) {
            if(st.charAt(i) != st.charAt(st.length() - 1 - i)) {
                System.out.println(st.length());
                return;
            }
        }
        // 입력값이 팰린드롬 이라면
        // 1. 2개 이상의 문자로 이루어진 팰린드롬 ==> 답(입력값의 길이 - 1)
        for(int i = 0;i < st.length() / 2;i++) {
            if(st.charAt(i) != st.charAt(i + 1)) {
                System.out.println(st.length() - 1);
                return;
            }
        }
        // 2. 하나의 문자로만 이루어진 팰린드롬 ==> 답(-1)
        System.out.println("-1");
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
