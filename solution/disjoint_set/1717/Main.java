//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/1cb796921b4c45b7946911e37a4216f3

import java.util.*;
import java.io.*;

public class Main {
    static int p[];
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        FastWriter wt = new FastWriter();
        
        int n = rd.nextInt();
        int m = rd.nextInt();
        
        p = new int[n + 1];
        // 초기화
        for(int i = 1;i <= n;i++) 
            p[i] = i;
        
        while(m --> 0) {
            int op = rd.nextInt();
            int a = rd.nextInt();
            int b = rd.nextInt();
            
            // 두 집합 합치기
            if(op == 0) 
                union(a, b);
            // a, b가 같은 집합에 속해있는지 확인
            else {
                if(find(a) == find(b)) wt.write("YES\n");
                else wt.write("NO\n");
            }
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
