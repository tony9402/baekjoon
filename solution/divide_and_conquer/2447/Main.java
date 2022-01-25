//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/afcb61a59b374cb999566aeaac14634d

import java.util.*;
import java.io.*;

public class Main {
    static boolean blank[][];
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        // 빠른 출력을 위해 FastWriter를 이용합니다
        // 미사용시 시간초과
        FastWriter wr = new FastWriter();
        
        int N = rd.nextInt();
        blank = new boolean[N][N];
        
        recur(0, 0, N);
        
        for(int i = 0;i < N;i++) {
            for(int j = 0;j < N;j++) {
                if(blank[i][j] == true) {
                    wr.write(" ");
                }
                else
                    wr.write("*");
            }
            wr.write("\n");
        }
        wr.flush();
        wr.close();
    }
    
    static void recur(int y, int x, int size) {
        int sz = size / 3;
        // sz가 0보다 작아지는 경우는 size가 1인 경우 
        // 진행할 필요 없으므로 return
        if(sz < 1) return;
        
        // 가운데 부분을 blank[i][j] = true로 하여
        // 공백 출력할 곳을 체크합니다
        for(int i = y + sz;i < y + sz * 2;i++) {
            for(int j = x + sz;j < x + sz * 2;j++) 
                blank[i][j] = true;
        }
        
        // 9등분 하여 다시 재귀를 진행합니다.
        for(int i = 0;i < 3;i++) {
            for(int j = 0;j < 3;j++) 
                recur(y + i * sz, x + j * sz, sz);
        }
    }
    
    static class FastWriter {
        BufferedWriter bw;
        String buffer = "";
        
        public FastWriter() {
            bw = new BufferedWriter(new OutputStreamWriter(System.out));
        }
        
        void write(String str) {
            try {
                bw.write(str);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        
        void flush() {
            try {
                bw.flush();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        
        void close() {
            try {
                bw.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
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
