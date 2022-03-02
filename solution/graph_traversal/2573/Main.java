//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/fa78ddbe4dd44b608496ae8b409f15b2

import java.util.*;
import java.io.*;

// 좌표 x, y를 저장하는 클래스
class Pair {
    int x, y;
    Pair(int y, int x) {
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static int N, M, ice_cnt, year;
    static int iceberg[][], melt_cnt[][];
    static boolean visited[][];
    static int dx[] = {0, 0, -1, 1};
    static int dy[] = {-1, 1, 0, 0};
    public static void main(String[] args) {
        FastReader rd = new FastReader();

        N = rd.nextInt();
        M = rd.nextInt();
        // 빙산전체를 저장하는 배열
        iceberg = new int[N + 10][M + 10];
        // 주변에 바다가 몇개인지 보고 얼마만큼 녹일지 저장하는 배열
        melt_cnt = new int[N + 10][M + 10];
        // bfs에 사용할 방문 확인 배열
        visited = new boolean[N + 10][M + 10];
        for(int i = 1;i <= N;i++) {
            for(int j = 1;j <= M;j++) {
                iceberg[i][j] = rd.nextInt();
                if(iceberg[i][j] != 0)
                    ice_cnt++;
            }
        }
        
        // 전체 다 녹을때까지 혹은 2개 이상으로 나누어질 때까지 반복
        // bfs로 몇개의 빙산이 있는지 확인
        // melt로 주변 바다를 세어 빙산을 녹임
        // ice_cnt는 얼음이 몇개인지, 즉 iceberg배열에서
        // 1이상의 값이 몇개인지 값을 가진다
        while(ice_cnt > 0) {
            bfs();
            year++;
            melt();
            for(int i = 1;i <= N;i++)
                Arrays.fill(visited[i], false);
        }
        System.out.println(0);
    }
    
    // bfs를 진행하면서 연결된 얼음의 개수가 몇개인지 센다(ice_size)
    // 만약 bfs가 끝나고 ice_size와 ice_cnt의 값이 다르다면
    // 두개 이상으로 나누어져 있다는 뜻이 된다
    // 하나의 얼음에서 연결된 모든 얼음을 세었는데 
    // 아직 세어지지 않은 얼음이 있다는 뜻이므로
    static void bfs() {
        int ice_size = 1;
        for(int i = 1;i <= N;i++) {
            for(int j = 1;j <= M;j++) {
                if(iceberg[i][j] > 0) {
                    Queue<Pair> q = new LinkedList<>();
                    q.add(new Pair(i, j));
                    visited[i][j] = true;
                    // 4방향으로 확인하면서 주변 연결된 얼음 수를 센다
                    while(!q.isEmpty()) {
                        Pair cur = q.poll();
                        for(int k = 0;k < 4;k++) {
                            int curx = cur.x + dx[k];
                            int cury = cur.y + dy[k];

                            if(curx < 1 || cury < 1) continue;
                            if(curx > M || cury > N) continue;
                            if(visited[cury][curx]) continue;
                            if(iceberg[cury][curx] <= 0) continue;

                            q.add(new Pair(cury, curx));
                            visited[cury][curx] = true;
                            ice_size++;
                        }
                    }
                    // 만약 연결된 얼음의 수와 전체 빙산의 얼음 수가 다르다면
                    // 2개 이상으로 분리된 경우 이므로 year출력 후 종료
                    if(ice_size != ice_cnt) {
                        System.out.println(year);
                        System.exit(0);
                    }
                    // 같으면 아직 빙산 덩어리가 1개라는 뜻
                    // 따라서 후에 빙산을 녹인다
                    else return;
                }
            }
        }
    }
    
    // 빙산을 녹이는 함수
    // 녹일 때 마다 ice_cnt값을 갱신 시켜준다
    static void melt() {
        ice_cnt = 0;
        for(int i = 1;i <= N;i++) {
            for(int j = 1;j <= M;j++) {
                // 얼음이 있는 부분에 4방향을 확인하여 바다 수를 센다
                if(iceberg[i][j] > 0) {
                    for(int k = 0;k < 4;k++) {
                        int cury = i + dy[k];
                        int curx = j + dx[k];

                        if(curx < 1 || cury < 1) continue;
                        if(curx > M || cury > N) continue;
                        
                        // 바다 수 만큼 melt_cnt배열을 증가시켜준다
                        if(iceberg[cury][curx] <= 0) 
                            melt_cnt[i][j]++;
                    }
                }
            }
        }
        
        // 바다의 수를 센 뒤 빙산을 녹여준다
        // 녹인 후 아직 얼음이 남아 있다면 ice_cnt를 증가시킨다
        for(int i = 1;i <= N;i++) {
            for(int j = 1;j <= M;j++) {
                iceberg[i][j] -= melt_cnt[i][j];
                if(iceberg[i][j] > 0) ice_cnt++;
            }
        }    
        
        for(int i = 1;i <= N;i++) 
            Arrays.fill(melt_cnt[i], 0);
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
