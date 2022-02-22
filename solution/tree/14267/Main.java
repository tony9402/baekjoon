//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/f67763b63b82494cae0c9b2efd214298

import java.util.*;
import java.io.*;

public class Main {
    static HashMap<Integer, Integer> map;
    static int n, m;
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        
        n = rd.nextInt();
        m = rd.nextInt();
        
        Tree tree = new Tree();
        // 사장의 직속상관 (-1)를 입력받아 버린다
        int u = rd.nextInt(); 
        // 각 사원별로 직속 상사만 저장한다
        for(int i = 2;i <= n;i++) {
            u = rd.nextInt();
            tree.insert(u, i);
        }
        
        // 입력받은 사원 별 칭찬 받은 총 횟수를 map에 
        map = new HashMap<Integer, Integer>(m + 1);
        for(int j = 0;j < m;j++) {
            int i = rd.nextInt();
            int w = rd.nextInt();
            
            map.put(i, map.getOrDefault(i, 0) + w);
        }
        tree.print(n);
    }
    
    static class Tree {
        // 직속 상사
        int in_neighbor[];
        int dp[];
        
        Tree() {
            in_neighbor = new int[n + 1];
            dp = new int[n + 1];
        }
        
        void insert(int u, int v) {
            in_neighbor[v] = u;
        }
        
        // 모든 사원들을 순회하면서 자신의 직속 상관이 칭찬받은 횟수에
        // 자신이 칭찬받은 횟수를 더하여 dp에 저장하고 출력한다
        void print(int n) {
            for(int i = 1;i <= n;i++) {
                dp[i] = dp[in_neighbor[i]] + map.getOrDefault(i, 0); 
                System.out.print(dp[i] + " ");
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
