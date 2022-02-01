//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/c137e72fa3a64178ace553194159e809

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        String st = rd.nextLine();
        
        // ^: 문자열의 시작
        // $: 문자열의 종료
        // (): 소괄호 안의 문자를 하나의 문자로 인식
        // +: 앞 문자가 하나 이상
        // |: 패턴 안에서 or 연산 이용
        String pattern = "^(100+1+|01)+$";
        if(st.matches(pattern))
            System.out.println("SUBMARINE");
        else
            System.out.println("NOISE");
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
