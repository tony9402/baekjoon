//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/7ed6e4f764034952a7feb5babc6fa087

import java.util.*;
import java.io.*;

public class Main {
    static String N;
    // canto[i]가 true이면 공백, false이면 '-'출력
    static boolean canto[];
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        // 빠른 출력을 위해 bufferedwriter클래스를 선언하여 사용합니다
        // 미사용시 시간초과
        FastWriter wr = new FastWriter();
        
        // EOF처리를 위해 N을 int형이 아닌 String형으로 입력 받습니다
        while((N = rd.nextLine()) != null) {
            int n = Integer.parseInt(N);
            int size = (int)Math.pow(3, n);
            canto = new boolean[size];
            
            recur(0, size);
            for(int i = 0;i < size;i++) {
                if(canto[i] == true)
                    wr.write(" ");
                else wr.write("-");
            }
            wr.write("\n");
            
            wr.flush();
            Arrays.fill(canto, false);
        }
        wr.close();
    }
    
    static void recur(int start, int size) {
        if(size == 1) return;
        
        // 3등분으로 나누어서 가운데 부분만 true(공백)으로 설정
        int sz = size / 3;
        for(int i = start + sz;i < start + 2 * sz;i++) 
            canto[i] = true;
        
        // 가운데는 공백이므로 살펴볼 필요가 없다
        // 따라서 양 옆 부분에 대해서만 다시 3등분 한다
        recur(start, sz);
        recur(start + sz * 2, sz);
    }
    
    static class FastWriter {
        BufferedWriter bw;
        
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
