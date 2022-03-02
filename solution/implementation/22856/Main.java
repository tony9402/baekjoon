//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/a764d7d50bda41d7bdfd17838af75e81

import java.util.*;
import java.io.*;

class Node {
    public int left, right, parent;
    Node(){
        this.left = -1;
        this.right = -1;
        this.parent = -1;
    }
    void setChildren(int left, int right) {
        this.left = left;
        this.right = right;
    }
    void setParent(int parent) {
        this.parent = parent;
    }
}

public class Main {
    static Node node[];
    static int count, N, end;
    static boolean visited[];
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        
        N = rd.nextInt();
        node = new Node[N + 10];
        visited = new boolean[N + 10];
        for(int i = 1;i <= N;i++) 
            node[i] = new Node();
        
        for(int i = 1;i <= N;i++) {
            int cur = rd.nextInt();
            int left = rd.nextInt();
            int right = rd.nextInt();
            node[cur].setChildren(left, right);
            if(left != -1) node[left].setParent(cur);
            if(right != -1) node[right].setParent(cur);
        }
        find_end(1);
        recur(1);
        // 구현 상 지나온 노드수를 세기 때문에 
        // 루트노드인 1도 세어져서 루트 1개를 빼준다
        System.out.println(count - 1);
    }
    // 순회의 끝 찾기. 항상 가장 오른쪽 노드가 순회의 끝 
    static void find_end(int cur) {
        end = cur;
        if(node[cur].right != -1)
            find_end(node[cur].right);
        else return;
    }
    // 유사 중위 순회 
    static void recur(int cur) {
        count++;
        visited[cur] = true;
        // 왼쪽 미방문
        if(node[cur].left != -1 && visited[node[cur].left] == false)  
            recur(node[cur].left);
        // 왼쪽 방문, 오른쪽 미방문
        else if(node[cur].right != -1 && visited[node[cur].right] == false)  
            recur(node[cur].right);
        // 왼쪽 방문, 오른쪽 방문, 순회의 끝일 때
        else if(cur == end) return; 
        // 왼쪽 방문, 오른쪽 방문, 순회의 끝이 아닐 때
        else recur(node[cur].parent);
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
