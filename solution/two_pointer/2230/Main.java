//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/d454024f7e5c41bc8893ab9ddcceed6e

import java.util.*;
import java.io.*;

public class Main {
    static ArrayList<Integer> A;
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        
        int N = rd.nextInt();
        int M = rd.nextInt();
        A = new ArrayList<Integer>(N + 10);
        
        for(int i = 0;i < N;i++)
            A.add(rd.nextInt());
        
        // 오름차순 정렬
        Collections.sort(A);
        
        // 0,1로 시작하여 (end의 값  - front의 값) < M 일때,
        // 두 값의 차이가 커져야 하므로 end를 증가시킵니다.
        // 그 외에는 min값을 갱신하고 front를 증가시킵니다.
        int front = 0, end = 1;
        int min = Integer.MAX_VALUE;
        while(front < N && end < N) {
            int dif = A.get(end) - A.get(front);
            if(dif < M) {
                end++;
                continue;
            }
            else {
                min = Math.min(min, dif);
                front++;
            }
        }
        System.out.println(min);
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
