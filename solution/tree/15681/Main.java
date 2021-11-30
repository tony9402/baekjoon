//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/0f61f373c1df4a91bb7dcc3a52dea9cf

import java.util.*;
import java.io.*;

/*
문제에서 주어진 힌트를 그대로 구현하였습니다.
*/

public class Main {
    static int[] subtreesize, parent;
    static ArrayList<Integer>[] tree, list;
	
    public static void main(String[] args) throws IOException {
        FastReader rd = new FastReader();

        int N = rd.nextInt();
        int R = rd.nextInt();
        int Q = rd.nextInt();
		
        tree = new ArrayList[N + 1];
        list = new ArrayList[N + 1];
        subtreesize = new int[N + 1];
        parent = new int[N + 1];
		
        for(int i = 0;i <= N;i++) {
            tree[i] = new ArrayList<Integer>();
            list[i] = new ArrayList<Integer>();
        }
		
        for(int i = 0;i < N - 1;i++) {
            int U = rd.nextInt();
            int V = rd.nextInt();
            list[U].add(V);
            list[V].add(U);
        }
	    
        //문제에 주어진 힌트
        makeTree(R, -1);
        countSubtreeNodes(R);
		
        for(int i = 0;i < Q;i++) {
            int U = rd.nextInt();
            System.out.println(subtreesize[U]);
        }
    }
	
    static void makeTree(int curNode, int p) {
        for(int node : list[curNode]) {
            if(node != p) {
                tree[curNode].add(node);
                parent[node] = curNode;
                makeTree(node, curNode);
            }
        }
    }
	
    static void countSubtreeNodes(int curNode) {
        subtreesize[curNode] = 1;//자신도 size에 포함
        for(int node : tree[curNode]) {
            countSubtreeNodes(node);
            subtreesize[curNode] += subtreesize[node];
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
