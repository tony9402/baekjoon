//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/ee82075c4ee544628f54b85c384ef616

import java.util.*;
import java.io.*;

public class Main {
    static int p[];
    static double ans;
    static Node node[];
    static ArrayList<Edge> edge;
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        
        int N = rd.nextInt();
        int M = rd.nextInt();
        p = new int[N + 1];
        node = new Node[N + 1];
        // 모든 노드들을 연결한다 
        // (1-2)와 (2-1)은 같으므로 절반만 필요
        edge = new ArrayList<Edge>(N * N / 2);
        
        for(int i = 1;i <= N;i++)
            p[i] = i;
        
        // 노드들의 좌표 저장
        for(int i = 1;i <= N;i++) {
            int X = rd.nextInt();
            int Y = rd.nextInt();
            
            node[i] = new Node(X, Y);
        }
        
        // 모든 노드들이 연결되도록 edge를 연결해준다
        // 각각 노드 별 거리도 계산하여 저장한다
        for(int i = 1;i < N;i++) {
            for(int j = i + 1;j <= N;j++) {
                double distance = getDistance(i, j);
                edge.add(new Edge(i, j, distance));
            }
        }
        
        // 이미 연결되어 있는 노드들을 입력 받아 union 해준다
        for(int i = 0;i < M;i++) {
            int n1 = rd.nextInt();
            int n2 = rd.nextInt();
            
            union(n1, n2);
        }
        
        // 크루스칼 알고리즘을 위해 거리를 오름차순으로 정렬한다
        Collections.sort(edge);
        // edge를 탐색하며 사이클을 이루지 않는 간선들을 차례로 선택한다
        for(Edge e : edge) {
            if(find(e.n1) != find(e.n2)) {
                ans += e.distance;
                union(e.n1, e.n2);
            }
        }
        System.out.printf("%.2f", ans);
    }
    
    // 노드의 index로 두 노드의 거리를 계산한다
    static double getDistance(int n1, int n2) {
        double x = Math.pow(node[n2].x - node[n1].x, 2);
        double y = Math.pow(node[n2].y - node[n1].y, 2);
        return Math.sqrt(x + y);
    }
    // 사이클 탐색을 위한 find함수
    static int find(int num) {
        if(p[num] == num) return num;
        else return p[num] = find(p[num]);
    }
    
    // 사이클 탐색을 위한 union함수
    static void union(int a, int b) {
        a = find(a);
        b = find(b);
        
        if(a < b) p[b] = a;
        else p[a] = b;
    }
    
    // 각 노드들의 x, y좌표를 저장한다
    static class Node {
        int x, y;
        Node(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
    
    // edge가 연결하는 두 노드의 index번호와 두 노드간 거리를 저장한다
    static class Edge implements Comparable<Edge> {
        int n1, n2;
        double distance;
        
        Edge(int n1, int n2, double distance){
            this.n1 = n1;
            this.n2 = n2;
            this.distance = distance;
        }
        
        @Override
        public int compareTo(Edge o) {
            return Double.compare(this.distance, o.distance);
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
