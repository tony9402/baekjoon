//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/d42746a577ac40cf8921ca94bbed14d6

import java.util.*;
import java.io.*;

public class Main {
    static int[] num = new int[100010];
    static int[] sum = new int[100010];

    public static void main(String[] args) {
        FastReader rd = new FastReader();

        int N = rd.nextInt();
        int M = rd.nextInt();

        // 1부터 i까지 합을 구해놓는다.
        for(int i = 1;i <= N;i++) {
            num[i] = rd.nextInt();
            sum[i] = sum[i - 1] + num[i];
        }

        // end까지의 합에서 begin전까지의 합을 빼면 그 중간 값들의 합이 나온다.
        // 매번 시행마다 더하면 시간초과
        for(int i = 0;i < M;i++) {
            int begin = rd.nextInt();
            int end = rd.nextInt();

            System.out.println(sum[end] - sum[begin - 1]);
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
