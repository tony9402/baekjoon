//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/27f36e5b50f247e69c5e8b3b89d57a5f

import java.util.*;
import java.io.*;

public class Main {
    static ArrayList<ArrayList<Node>> graph;
    static int d[];
    static boolean visited[];
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        
        int V = rd.nextInt();
        int E = rd.nextInt();
        int K = rd.nextInt();
        
        visited = new boolean[V + 10];
        // d[i]는 i노드까지 최단 경로의 경로값을 가진다
        d = new int[V + 10];
        // 출발정점은 0, 나머지는 int형 최대값으로 초기화
        Arrays.fill(d, Integer.MAX_VALUE);
        d[K] = 0;
        
        // 그래프 초기화
        graph = new ArrayList<ArrayList<Node>>();
        for(int i = 0;i <= V;i++) 
            graph.add(new ArrayList<Node>());
        
        // 그래프 만들기
        for(int i = 0;i < E;i++) {
            int u = rd.nextInt();
            int v = rd.nextInt();
            int w = rd.nextInt();
            
            graph.get(u).add(new Node(v, w));
        }
        
        dijkstra(K);
        
        for(int i = 1;i <= V;i++) {
            if(d[i] == Integer.MAX_VALUE) 
                System.out.println("INF");
            else
                System.out.println(d[i]);
        }
    }
    
    static void dijkstra(int start) {
        // 우선순위 큐를 이용하여 가중치를 기준으로 가장 가까운 노드부터 방문
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(start, 0));
        
        // 모든 노드를 출발점으로부터 가까운 순서대로
        // 한번씩 방문하게 된다
        while(!pq.isEmpty()) {
            Node cur = pq.poll();
            int dest = cur.dest;
            // 이미 방문했던 노드는 또 확인하지 않는다
            if(visited[dest]) continue;
            visited[dest] = true;
            
            // 최소값으로 갱신하고 큐에 넣는다
            for(Node next : graph.get(dest)) {
                d[next.dest] = Math.min(d[next.dest], d[dest] + next.weight);
                pq.add(new Node(next.dest, d[next.dest]));
            }
        }
    }
    
    static class Node implements Comparable<Node>{
        int dest, weight;
        Node(int dest, int weight){
            this.dest = dest;
            this.weight = weight;
        }
        
        @Override
        public int compareTo(Node o) {
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
