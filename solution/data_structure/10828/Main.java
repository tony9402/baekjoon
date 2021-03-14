import java.lang.*;
import java.util.*;
import java.io.*;

public class Main{
    static public void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // Scanner 쓰면 TLE
        BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out)); // System.out.* 로 써도 가능은 함

        int N = Integer.parseInt(br.readLine());
        
        Stack<String> stack = new Stack<>(); // 값 계산 하는게 없으니 문자열로만 해도 됨.
        for(int i=0;i<N;i++){
            String[] Line = br.readLine().split(" "); 
            String cmd = Line[0]; 

            if(cmd.equals("push")) {
                stack.push(Line[1]);
            }
            else if(cmd.equals("pop")) {
                if(stack.empty()){
                    wr.write("-1");
                }
                else {
                    wr.write(stack.peek());
                    stack.pop();
                }
                wr.newLine();
            }
            else if(cmd.equals("size")) {
                wr.write(String.format("%d", stack.size()));
                wr.newLine();
            }
            else if(cmd.equals("empty")) {
                wr.write(stack.empty() ? "1" : "0");
                wr.newLine();
            }
            else if(cmd.equals("top")) {
                if(stack.empty()){
                    wr.write("-1\n");
                }
                else {
                    wr.write(stack.peek() + "\n");
                }
            }
        }
        
        wr.flush();
        wr.close();
    }
}
