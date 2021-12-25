//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/de782e0aed93403384ae477b960ab1a6

import java.util.*;
import java.io.*;

class Pair{
    public int idx, w;
    Pair(int idx, int w){
        this.idx = idx; // index번호
        this.w = w; // weight
    }
}

public class Main {
    static ArrayList<Pair> tree[];
    static boolean visited[];
    static int weight[];
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        
        int n = rd.nextInt();
        // 입력받은 트리를 저장합니다.
        tree = new ArrayList[n + 10];
        // bfs에서 방문 유무를 저장합니다.
        visited = new boolean[n + 10];
        // i번째 노드까지 오면서 가중치의 합을 저장합니다.
        weight = new int[n + 10];
        
        // 인접리스트를 이용하여 그래프를 만듭니다.
        for(int i = 0;i <= n;i++) 
            tree[i] = new ArrayList<Pair>();
        
        for(int i = 0;i < n - 1;i++) {
            int p = rd.nextInt(); // parent
            int c = rd.nextInt(); // child
            int w = rd.nextInt(); // weight
            tree[p].add(new Pair(c, w));
            tree[c].add(new Pair(p, w));
        }
        
        // 시작노드 1에서 가장 먼 노드를 구한 다음 
        // 그 노드를 시작점으로 가장 먼 노드까지의 거리가 지름이 됩니다.
        Pair a = bfs(1); // 1번 노드로부터 가장 먼 노드
        Pair b = bfs(a.idx); // 앞에서 구한 노드로부터 가장 먼 노드
        
        System.out.println(b.w);
    }
 
    public static Pair bfs(int start) {
        int max_weight = 0;
        int max_idx = 0;
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        visited[start] = true;
        
        while(!q.isEmpty()) {
            int cur = q.poll();
            
            for(Pair p : tree[cur]) {
                if(visited[p.idx] == true) continue; // 방문한 노드
                // 미방문
                visited[p.idx] = true;
                weight[p.idx] = p.w + weight[cur];
                // 가장 먼 노드의 인덱스와 가중치를 저장합니다.
                if(max_weight < weight[p.idx]) {
                    max_weight = weight[p.idx];
                    max_idx = p.idx;
                }
                q.add(p.idx);
            }
        }
        
        // 다음 bfs사용을 위해 초기화 합니다.
        Arrays.fill(visited, false);
        Arrays.fill(weight, 0);
        
        return new Pair(max_idx, max_weight);
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
