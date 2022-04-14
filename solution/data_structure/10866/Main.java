// Authored by : KimJeongSoo723
// Co-authored by : -
// Link : https://www.acmicpc.net/problem/10866


import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        FastReader input = new FastReader();
        Deque<Integer> deq = new LinkedList<>();
        StringBuilder sb = new StringBuilder(); // 매 case마다 System.out.println을 쓰면 시간초과가 날수 있습니다.
        int n = input.nextInt();

        while(n-- > 0){
            boolean empty = deq.isEmpty();

            switch (input.next()) {
                case "push_front": // push_front와 push_back의 경우 input의 다음토큰이 확정적으로 정수 X가 됩니다.
                    deq.addFirst(input.nextInt());
                    break;
                case "push_back":
                    deq.addLast(input.nextInt());
                    break;
                case "pop_front":
                    if (empty) sb.append("-1" + "\n");
                    else sb.append(deq.pollFirst() + "\n");
                    break;
                case "pop_back":
                    if (empty) sb.append("-1" + "\n");
                    else sb.append(deq.pollLast() + "\n");
                    break;
                case "size":
                    sb.append(deq.size() + "\n");
                    break;
                case "empty":
                    if (empty) sb.append("1" + "\n");
                    else sb.append("0" + "\n");
                    break;
                case "front":
                    if (empty) sb.append("-1" + "\n");
                    else sb.append(deq.peekFirst() + "\n");
                    break;
                case "back":
                    if (empty) sb.append("-1" + "\n");
                    else sb.append(deq.peekLast() + "\n");
                    break;
                default:
                    break;
            }
        }
        System.out.print(sb);
    }




    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() throws IOException{
            br = new BufferedReader(new InputStreamReader(System.in)); //백준 제출 시 주석해제를 하면 됩니다.
            //br = new BufferedReader(new FileReader("input.txt")); //IDE 실행 시 주석해제를 하면 됩니다.
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
