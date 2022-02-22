//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/ff49a95e179e4b5c985d61597f255c7b

import java.util.*;
import java.io.*;

public class Main {
    static int caseIdx = 1;
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        
        while(true) { // case를 반복하는 while문
            Tree tree = new Tree();
            // 입력받는 노드들의 idx를 저장할 set
            HashSet<Integer> set = new HashSet<>();
            // 입력받는 (출발, 도착)노드를 저장할 Pair객체
            ArrayList<Pair> pair = new ArrayList<>();
            while(true) { // 간선을 입력받는 while문
                int u = rd.nextInt();
                int v = rd.nextInt();
                if(u == -1 && v == -1) return;
                if(u == 0 && v == 0) break;
                
                // set에 입력받는 노드들이 중복제거되어 들어감
                set.add(u);
                set.add(v);
                
                pair.add(new Pair(u, v));
            }
            tree.Insert(set, pair);
            
            if(tree.bfs(set)) tree.print(true);
            else tree.print(false);
        }   
    }
    
    static class Pair {
        int first, second;
        Pair(int first, int second){
            this.first = first;
            this.second = second;
        }
    }
    
    static class Tree {
        // out_neighbor는 노드의 idx와 그 노드의 out_neighbor의 idx를 저장한다
        HashMap<Integer, ArrayList<Integer>> out_neighbor;
        // in_neighbor는 노드의 idx와 그 노드의 부모노드(in_neighbor)의 개수를 저장한다
        HashMap<Integer, Integer> in_neighbor;
        
        Tree() {
            out_neighbor = new HashMap<Integer, ArrayList<Integer>>();
            in_neighbor = new HashMap<>();
        }
        
        void Insert(HashSet<Integer> set, ArrayList<Pair> pair) {
            // 입력받는 노드들의 idx를 key로 map에 저장한다
            for(int i : set) {
                out_neighbor.put(i, new ArrayList<Integer>());
                in_neighbor.put(i, 0);
            }
            
            // 입력받은 pair를 저장한다. 또한 in_neighbor의 개수도 센다
            for(Pair p : pair) {
                int u = p.first;
                int v = p.second;
                
                out_neighbor.get(u).add(v);
                in_neighbor.put(v, in_neighbor.get(v) + 1);
            }
        }
        
        boolean bfs(HashSet<Integer> set) {
            Queue<Integer> q = new LinkedList<>();
            
            // 시작할 루트를 찾는다. 루트는 3가지의 경우로 나누어진다
            int root = findRoot(set);
            if(root == 0) return true;
            else if(root == -1) return false;
            
            // 루트를 찾아 bfs를 시작한다
            in_neighbor.put(root, 1);
            q.add(root);
            
            while(!q.isEmpty()) {
                int cur = q.poll();
                for(int child : out_neighbor.get(cur)) {
                    // 만약 이미 방문된 자식을 또 방문하고자 하는 경우
                    // 즉 부모노드(in_neighbor의 수가 1개 이상인 경우
                    // 트리 조건에 만족하지 않는다. false 리턴
                    if(in_neighbor.get(child) > 1) 
                        return false;
                    
                    in_neighbor.put(child, 1);
                    q.add(child);
                }
            }
            
            // 루트가 여러개인 경우 
            // 부모노드가 없는 노드가 여러개인 경우(in_neighbor의 수가 0인 노드가 여러개)
            // 트리조건에 만족하지 않으므로 false 리턴
            for(int i : set) {
                if(in_neighbor.get(i) == 0) 
                    return false;
            }
            // 정상적으로 bfs탐색이 되었다면 true를 리턴한다
            return true;
        }

        // return 0는 set의 size가 0일 때, 즉 노드가 없어서 반드시 tree일 때
        // return i는 정상적으로 루트를 찾아서 루트 idx를 리턴할 때
        // return -1은 노드는 있지만 루트가 없는 경우일 때
        int findRoot(HashSet<Integer> set) {
            if(set.size() == 0) return 0;
            for(int i : set) {
                if(in_neighbor.get(i) == 0) 
                    return i;
            }
            return -1;
        }
        
        void print(boolean flag) {
            if(flag) System.out.println("Case " + caseIdx++ + " is a tree.");
            else System.out.println("Case " + caseIdx++ + " is not a tree.");
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
