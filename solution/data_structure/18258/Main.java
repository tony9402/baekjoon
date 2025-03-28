// Authored by : semInDev
// Co-authored by : -
// Link : https://www.acmicpc.net/problem/18258

import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
        FastReader input = new FastReader();
        
        Deque<Integer> deque = new ArrayDeque<>(); // back명령어를 사용하기 위해 deque이용
        StringBuilder sb = new StringBuilder();
        
        int N = input.nextInt();
		while(N-->0) {
			String cmd = input.next();			
			switch (cmd) {
				case "push":
					int X = input.nextInt();
					deque.add(X);
					break;
				case "pop":
					if(deque.isEmpty()) sb.append(-1+"\n");
					else sb.append(deque.poll()+"\n");
					break;
				case "size":
					sb.append(deque.size()+"\n");
					break;
				case "empty":
					if(deque.isEmpty()) sb.append(1+"\n");
					else sb.append(0+"\n");
					break;
				case "front":
					if(deque.isEmpty()) sb.append(-1+"\n");
					else sb.append(deque.peekFirst()+"\n");
					break;
				case "back":
					if(deque.isEmpty()) sb.append(-1+"\n");
					else sb.append(deque.peekLast()+"\n");
			}
		}
        System.out.print(sb);
	}
	
    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() throws IOException{
        	br = new BufferedReader(new InputStreamReader(System.in)); //백준 제출 시 주석해제를 하면 됩니다.
        	// br = new BufferedReader(new FileReader("input.txt")); //IDE 실행 시 주석해제를 하면 됩니다.
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