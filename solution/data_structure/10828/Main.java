// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/011509a1ee6b4edf8c2b2b2630b9822f
import java.lang.*;
import java.util.*;
import java.io.*;

public class Main{
    static public void main(String[] args) {
        FastReader rd = new FastReader();

        int N = rd.nextInt();
        
        Stack<String> stack = new Stack<>(); 

        StringBuilder out = new StringBuilder();
        for(int i=0;i<N;i++){
            String[] Line = rd.nextLine().split(" ");
            String cmd = Line[0]; 

            if(cmd.equals("push")) {
                stack.push(Line[1]);
            }
            else if(cmd.equals("pop")) {
                if(stack.empty()){
                    out.append("-1");
                }
                else {
                    out.append(stack.peek());
                    stack.pop();
                }
                out.append("\n");
            }
            else if(cmd.equals("size")) {
                out.append(stack.size() + "\n");
            }
            else if(cmd.equals("empty")) {
                out.append(stack.empty() ? "1" : "0");
                out.append("\n");
            }
            else if(cmd.equals("top")) {
                if(stack.empty()){
                    out.append("-1\n");
                }
                else {
                    out.append(stack.peek() + "\n");
                }
            }
        }
        System.out.print(out);
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
        double nextDouble() { return Double.parseDouble(next()); }
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
