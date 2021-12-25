//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/183e8c3f134847ccb55fc85f0d072a61

import java.util.*;
import java.io.*;

class Pair {
    int x, y;
    Pair(int x, int y){
        this.x = x; // x는 건물의 높이를 갖는다.
        this.y = y; // y는 건물의 위치를 갖는다.
    }
    int getX() {
        return x;
    }
    int getY() {
        return y;
    }
}

public class Main {
    static int[] receive = new int[500010]; //수신받는 건물 위치 저장
    static Stack<Pair> stack = new Stack<>(); 
    
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        
        int N = rd.nextInt();
        stack.push(new Pair(rd.nextInt(), 1));
        
        for(int i = 2;i <= N;i++) {
            int n = rd.nextInt();
            
            while(true) {
                // 우선 스택이 비어있는지 확인합니다
                // 비어있으면 자신보다 높은 건물은 앞에 존재하지 않으므로
                // receive 값은 0입니다
                if(stack.isEmpty() == true) {
                    stack.push(new Pair(n, i));
                    break;
                }
                // 자신보다 작은 건물들을 stack에서 pop합니다
                else if(stack.peek().getX() < n) 
                    stack.pop();
                // stack을 보다가 자기보다 높은 건물을 발견하면
                // 그 건물의 위치를 receive에 저장하고
                // stack에 push합니다
                else {
                    receive[i] = stack.peek().getY();
                    stack.push(new Pair(n, i));
                    break;
                }
            }
        }
        
        for(int i = 1;i <= N;i++) {
            System.out.print(receive[i] + " ");
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
