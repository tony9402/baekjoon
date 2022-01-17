//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/a5fb4121a1b945779fe1e4c74703bf24

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        
        long n = rd.nextInt();
        long k = rd.nextLong();
        
        // 색종이 조각의 개수를 구하는 식
        // 가로로 자르는 횟수 row
        // 세로로 자르는 횟수 col 라 한다면
        // (row + 1) * (col + 1) 이다. (row + col == N)
        
        long left = 0;
        long right = n / 2;
        while(left <= right) {
            long row = (left + right) / 2; // 이분탐색 mid 역할
            long col = n - row;
            
            long pieces = (row + 1) * (col + 1);
            if(pieces == k) {
                System.out.println("YES");
                return;
            }
            // 조각 수가 더 많으므로 row 와 col사이의 
            // 값 차이를 벌린다
            else if(pieces > k) 
                right = row - 1;
            // k보다 조각수가 작으므로 row와 col사이의
            // 값 차이를 좁혀 조각 수를 많게 만들어준다
            else
                left = row + 1;
        }
        System.out.println("NO");
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
