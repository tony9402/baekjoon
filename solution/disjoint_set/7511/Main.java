//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/e82fb21779ba4cec90482332027edb74

import java.util.*;
import java.io.*;

public class Main {
    static int p[];
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        FastWriter wt = new FastWriter();
        
        int t = rd.nextInt();
        for(int i = 1;i <= t;i++) {
            int n = rd.nextInt();
            int k = rd.nextInt();
            
            p = new int[n];
            for(int j = 0;j < n;j++) 
                p[j] = j;
            
            // 두 집합 합치기
            while(k --> 0) {
                int a = rd.nextInt();
                int b = rd.nextInt();
                union(a, b);
            }

            wt.write("Scenario " + i + ":\n");

            int m = rd.nextInt();
            for(int j = 1;j <= m;j++) {
                int a = rd.nextInt();
                int b = rd.nextInt();

                if(find(a) == find(b)) wt.write("1\n");
                else wt.write("0\n");
            }
            wt.write("\n");
        }
        wt.flush();
        wt.close();
    }
    
    static void union(int a, int b) {
        a = find(a);
        b = find(b);
        
        if(a == b) return;
        if(a < b) p[b] = a;
        else p[a] = b;
    }
    
    static int find(int num) {
        if(p[num] == num) return num;
        return p[num] = find(p[num]);
    }
    
    static class FastWriter {
        BufferedWriter bw;
        
        public FastWriter() {
            bw = new BufferedWriter(new OutputStreamWriter(System.out));
        }
        
        void write(String str) {
            try {
                bw.write(str);
            } 
            catch (IOException e) {
                e.printStackTrace();
            }
        }
        
        void flush() {
            try {
                bw.flush();
            } 
            catch (IOException e) {
                e.printStackTrace();
            }
        }
        
        void close() {
            try {
                bw.close();
            } 
            catch (IOException e) {
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
