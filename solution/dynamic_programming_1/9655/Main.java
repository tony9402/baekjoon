//Authored by : suin8
//Co-authored by : tony9402
//Link : http://boj.kr/096e8e82144f450ab19b16bcf62cc83b
import java.util.*;
import java.io.*;

public class Main {
    static int DP[] = new int[1001];
    public static void main(String[] args) {
        FastReader rd = new FastReader();

        // 짝수일때는 창영이가, 홀수일때는 상근이가 이기게 됩니다.
        // 반드시 상근이가 먼저 시작하고 1,3 홀수개 만큼 가져가기 때문.
        // System.out.println((N % 2 == 0) ? "CY" : "SK");

        int N = rd.nextInt();
        // 1 : 상근, 2 : 창영
        DP[1] = 1;
        for(int i = 1; i < 1000; i++) {
            if(DP[i + 1] == 0) DP[i + 1] = 3 - DP[i];
            if(i + 3 <= 1000) DP[i + 3] = 3 - DP[i];
        }
        System.out.println((DP[N] % 2 == 0 ? "CY" : "SK"));
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
