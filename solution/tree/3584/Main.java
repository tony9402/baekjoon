//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/2b48d830901a4b2d93f3b4a82e7104e4

import java.util.*;
import java.io.*;

public class Main {
    static int[] parent;
    static Vector<Integer> comm_1, comm_2;
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        
        int T = rd.nextInt();
        while(T --> 0) { // T번 반복합니다.
            int N = rd.nextInt();
            parent = new int[N + 10];

            // comm_1, comm_2는 공통조상을 찾아야 할 수 comm1, comm2의
            // 자신을 포함한 루트까지의 조상 값을 저장하는 벡터입니다.
            comm_1 = new Vector<Integer>();
            comm_2 = new Vector<Integer>();
            
            for(int i = 0;i < N - 1;i++) {
                int A = rd.nextInt(); // parent
                int B = rd.nextInt(); // child
                parent[B] = A;
            }

            int comm1 = rd.nextInt();
            int comm2 = rd.nextInt();
            // 첫 번째 수의 자신포함 모든 조상를 벡터에 넣습니다.
            // parent[i]값이 0이면 루트라는 뜻입니다.
            while(comm1 != 0) {
                comm_1.add(comm1);
                comm1 = parent[comm1];
            }

            // 두 번째 수의 자신포함 모든 조상를 벡터에 넣습니다.
            while(comm2 != 0) {
                comm_2.add(comm2);
                comm2 = parent[comm2];
            }

            // 두 개의 벡터를 하나씩 비교하면서 가장 먼저 겹치는 수가
            // 첫 번째 공통 조상의 index입니다.
            for(int i : comm_1) {
                if(comm_2.indexOf(i) != -1) {
                    System.out.println(i);
                    break;
                }
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
