//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/97e688fe24824fb093cecef394308b8f

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

            int cnt = 0;
            int min = Integer.MAX_VALUE;
            // i번째 인덱스를 기준으로 i와 mid인덱스 값의 합이
            // k와 가장 근사한 mid값을 이분탐색으로 찾습니다
            for(int i = 0;i < S.size();i++) {
                int left = i + 1;
                int right = S.size() - 1;
                while(left <= right) {
                    int mid = (left + right) / 2;
                    int sum = S.get(i) + S.get(mid);
                    int diff = Math.abs(k - sum);
                    
                    if(diff < min) {
                        min = diff;
                        cnt = 1;
                    }
                    else if(diff == min) cnt++;
                    
                    if(sum > k) right = mid - 1;
                    else if(sum == k) break;
                    else left = mid + 1;
                }
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
