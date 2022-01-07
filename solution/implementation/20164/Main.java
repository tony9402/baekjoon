//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/a1cece16a1f445718163e49d0be98469

import java.util.*;
import java.io.*;

public class Main {
    static int max_cnt = 0, min_cnt = Integer.MAX_VALUE;
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        
        String N = rd.next();

        recur(N, 0);
        System.out.println(min_cnt + " " + max_cnt);
    }
    
    // 재귀 형식으로 모든 자를 수 있는 경우의 수를 살핍니다 ==> 브루트포스 Alg.
    static void recur(String N, int cnt) {
        int len = N.length();
        cnt += odd_cnt(N, len);
        
        // 자리수가 1이 되었을 때, 본 홀수로 max, min값을 갱신합니다
        if(len == 1) { // 한 자리 숫자
            max_cnt = Math.max(max_cnt, cnt);
            min_cnt = Math.min(min_cnt, cnt);
            return ;
        }
        // 자리수가 2일 때, 두 수로 나누어 더하고 새로운 수로 생각합니다
        else if(len == 2) { // 두 자리 숫자
            int new_N = N.charAt(0) + N.charAt(1) - (2 * '0');
            recur(Integer.toString(new_N), cnt);
        }
        // 자리수가 3이상일 때, 3개의 수로 나누는 모든 경우의 수를 살피고
        // 나눈 수를 더하여 새로운 수로 생각합니다 (재귀)
        else { // 세 자리 이상 숫자
            int partition1 = 1, partition2 = 2;
            while(partition1 <= len - 2 && partition2 <= len - 1) {
                int part1 = Integer.parseInt(N.substring(0, partition1));
                int part2 = Integer.parseInt(N.substring(partition1, partition2));
                int part3 = Integer.parseInt(N.substring(partition2, len));
                
                int new_N = part1 + part2 + part3;
                recur(Integer.toString(new_N), cnt);
                
                partition2++;
                if(partition2 == len) {
                    partition1++;
                    partition2 = partition1 + 1;
                }
            }
        }
    }
    
    // 숫자에서 홀수 개수를 카운트 하고 리턴합니다.
    // 각 자리수 별로 2로 나누어 나머지가 1이면 cnt를 증가시킵니다
    static int odd_cnt(String N, int len) {
        int cnt = 0;
        for(int i = 0;i < len;i++) {
            if((N.charAt(i) - '0') % 2 == 1)
                cnt++;
        }
        return cnt;
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
