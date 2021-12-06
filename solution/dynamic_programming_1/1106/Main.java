//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/f27ceec311074b119fc847208aad7a4a

import java.util.*;
import java.io.*;

class Pair{
    private int cost, customer;
    Pair(int cost, int customer) {
        this.cost = cost;
        this.customer = customer;
    }
    public int getCo() { return cost; }
    public int getCu() { return customer; }
}

public class Main {
    // dp[i]는 i의 비용으로 몇명의 고객을 늘릴 수 있는지
    // 최대 : 100원으로 1명의 인원이 늘어날 수 있고 1000명을 모집해야 한다면
    // 100 * 1000 = 100000 만큼 필요 
    static Pair[] city = new Pair[30]; // 도시의 수
    static int[] dp = new int[100010]; 
    
    public static void main(String[] args) {
        FastReader rd = new FastReader();

        int C = rd.nextInt();
        int N = rd.nextInt();

        for(int i = 0;i < N;i++) {
            int x = rd.nextInt();
            int y = rd.nextInt();
            city[i] = new Pair(x,y);
        }

        // dp[i], 즉 i의 돈으로 홍보 할 수 있는 최대의 인원을 각 도시를 돌면서 확인하여 최대값으로 갱신합니다.
        for(int i = 1;i < 100001;i++) {
            for(int j = 0;j < N;j++) {
                if(city[j].getCo() <= i) 
                    dp[i] = Math.max(dp[i], dp[i - city[j].getCo()] + city[j].getCu());
            }
            // dp[i]가 홍보 해야 할 인원을 만족하면 i는 최소비용
            if(dp[i] >= C) {
                System.out.println(i);
                break;
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
