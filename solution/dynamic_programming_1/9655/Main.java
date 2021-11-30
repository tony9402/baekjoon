//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/945004772e74412fa8f1094de077eac4

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        FastReader rd = new FastReader();
		
        int N = rd.nextInt();
		
        //짝수일때는 창영이가, 홀수일때는 상근이가 이기게 됩니다.
        System.out.println((N % 2 == 0) ? "CY" : "SK");
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
