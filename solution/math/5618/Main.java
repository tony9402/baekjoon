//Authored by : suin8
//Co-authored by : tony9402
//Link : http://boj.kr/41ff4237225e495ba67f4ae2477eacc9

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        FastReader rd = new FastReader();

        int n = rd.nextInt();
        int num1 = 0, num2 = 0, num3 = 0;
        num1 = rd.nextInt();
        num2 = rd.nextInt();
        if(n == 3) {
            num3 = rd.nextInt();
        }
        
        // 1부터 차례대로 2개 또는 3개의 숫자가 모두
        // 나누어지면 공약수 => 출력
        for(int i = 1;i <= num1; i++) { 
            if(num1 % i == 0 && num2 % i == 0 && num3 % i == 0)
                System.out.println(i);
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
