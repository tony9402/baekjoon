//Authored by : suin8
//Co-authored by : tony9402
//Link : http://boj.kr/a390775f4af44af3af4239329e91fdcb

import java.util.*;
import java.io.*;

public class Main {
    static int[] num = new int[200010];
    static int[] count = new int[100010];

    public static void main(String[] args) {
        FastReader rd = new FastReader();

        int N = rd.nextInt();
        int K = rd.nextInt();

        for(int i = 1;i <= N;i++)
            num[i] = rd.nextInt();

        // 투포인터로 풀이
        // start와 end사이에 겹치는 수가 K개 이하일 때는 end증가
        // K개 초과일 때는 start를 늘려가며 겹치는 수가 빠질때까지 begin증가
        int max = 0;
        for(int begin = 1, end = 1; begin <= N; begin ++) {
            while(end <= N && count[num[end]] < K) {
                count[num[end]] ++;
                end ++;
            }
            max = Math.max(end - begin, max);
            count[num[begin]] --;
        }
        System.out.println(max);
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
