//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/7f20b69d2f604d2aaf5509387c9fb531

import java.util.*;
import java.io.*;

public class Main {
    static ArrayList<Edge> edge;
    static int p[];
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        
        int N = rd.nextInt();
        int M = rd.nextInt();
        edge = new ArrayList<Edge>(N + 1);
        p = new int[N + 1];
        for(int i = 1;i <= N;i++)
            p[i] = i;
        
        for(int i = 0;i < M;i++) {
            int a = rd.nextInt();
            int b = rd.nextInt();
            int c = rd.nextInt();
            
            edge.add(new Edge(a, b, c));
        }
        // 오름차순 정렬
        Collections.sort(edge);
        
        int ans = 0;
        for(Edge e : edge) {
            // 사이클이 아닌 경우에만 포함시킨다
            if(find(e.n1) != find(e.n2)) {
                ans += e.weight;
                union(e.n1, e.n2);
            }
        }
        System.out.println(ans);
    }
    
    static int find(int num) {
        if(p[num] == num) return num;
        else return p[num] = find(p[num]);
    }
    
    static void union(int a, int b) {
        a = find(a);
        b = find(b);
        
        if(a < b) p[b] = a;
        else p[a] = b;
    }
    
    static class Edge implements Comparable<Edge> {
        int n1, n2, weight;
        
        Edge(int a, int b, int c) {
            this.n1 = a;
            this.n2 = b;
            this.weight = c;
        }
        
        @Override
        public int compareTo(Edge o) {
            return this.weight - o.weight;
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
