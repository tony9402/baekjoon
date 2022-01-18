//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/6392a81910214ca2b181968ceabbc254

import java.util.*;
import java.io.*;

public class Main {
    static ArrayList<Integer> S = new ArrayList<Integer>();
    public static void main(String[] args) {
        FastReader rd = new FastReader();

        int t = rd.nextInt();
        while(t --> 0) {
            int n = rd.nextInt();
            int k = rd.nextInt();

            // 오름차순으로 정렬합니다.
            for(int i = 0;i < n;i++)
                S.add(rd.nextInt());
            Collections.sort(S);

            int left = 0;
            int right = S.size() - 1;
            int min = Integer.MAX_VALUE;
            int cnt = 0;
            // 배열의 처음과 끝에 포인터를 두고 시작합니다
            // sum값이 k보다 작으면 sum값이 커져야 하므로 left증가
            // sum값이 k보다 크면 sum값이 작아져야 하므로 right감소
            while(left < right) {
                int sum = S.get(left) + S.get(right);
                int diff = Math.abs(k - sum);

                if(diff < min) {
                    min = diff;
                    cnt = 1;
                }
                else if(diff == min) cnt++;

                if(sum < k) left++;
                else if(sum == k) {
                    left++;
                    right--;
                }
                else right--;
            }
            System.out.println(cnt);

            S.clear();
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
