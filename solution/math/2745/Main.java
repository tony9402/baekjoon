//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/31dab421076b458aac0065580a31cbe2

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) {
        FastReader rd = new FastReader();
		
        String N = rd.next();
        int B = rd.nextInt();
		
        int num = 0;
        int digit = 0;
        for(int i = N.length() - 1; i >= 0; i--) {
            if(N.charAt(i) >= 65) // 문자 A~Z == 정수(65~90) -> 10진법(-55)
                num += (N.charAt(i) - 55) * Math.pow(B, digit);
            else  // 문자 0~9 == 십진법(48~57)
                num += (N.charAt(i) - 48) * Math.pow(B, digit);

            digit++;
        }
		
        System.out.print(num);
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
