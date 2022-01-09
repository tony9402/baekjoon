//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/452eb01b7a1c4104b17f8ce24a1bccf2

import java.util.*;
import java.io.*;

public class Main {
    static ArrayList<ArrayList<Integer>> friend;
    static int N, M, ans;
    static boolean visited[];
    public static void main(String[] args) {
        FastReader rd = new FastReader();

        N = rd.nextInt();
        M = rd.nextInt();
        
        visited = new boolean[N + 10];
        friend = new ArrayList<ArrayList<Integer>>(N + 10);
        for(int i = 0;i < N;i++)
            friend.add(new ArrayList<Integer>());
        
        while(M --> 0) {
            int a = rd.nextInt();
            int b = rd.nextInt();
            friend.get(a).add(b);
            friend.get(b).add(a);
        }
        // 각각 친구마다 dfs로 깊이 4인것을 확인한다.
        for(int i = 0;i < N;i++) 
            dfs(i, 0);
        
        System.out.println(0);
    }
    
    static void dfs(int cur, int depth) {
        visited[cur] = true;
        // 깊이가 4이면 조건 관계 만족
        // 1출력 후 종료
        if(depth == 4) {
            System.out.println(1);
            System.exit(0);
        }
        // 아직 깊이가 4가 아니고 방문되지 않은 경우
        // 그 친구를 방문하고 깊이를 1 증가시킨다
        for(int i : friend.get(cur)) {
            if(visited[i] == false)
                dfs(i, depth + 1);
        }
        visited[cur] = false;
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
