// Authored by : KimJeongSoo723
// Co-authored by : -
// Link : https://www.acmicpc.net/problem/2346


import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        FastReader input = new FastReader();
        int n = input.nextInt();
        int [] movearr = new int [n];
        Deque <Integer> deq = new LinkedList<>();
        StringBuilder sb = new StringBuilder();

        for(int i=0;i<n;i++) deq.offer(i);
        for(int i=0;i<n;i++) movearr[i]=input.nextInt();

        while(deq.size()>0){
            sb.append(deq.peek()+1 + " "); // 터지는 풍선의 번호는 deq.peek()+1 입니다.
            int move = movearr[deq.peek()]; // 풍선에 담긴 값입니다.
            if(deq.size()==1){
                break;
            }
            if(move>0) {
                deq.poll();
                move--; // move가 양수인경우에는 deq.poll()을 수행함으로써 move를 한번한것과 동일한 효과가 납니다.
                move = move%deq.size(); // 예시로, 원형 deq에서 deq size는 3인데 move를 97번 해야된다면 move를 1번한것과 동일합니다. 이 연산을 수행안하고 그냥 move값을 대입하면 메모리초과가 날 수 있습니다.
                while (move > 0) {
                    deq.offer(deq.poll()); // 가장 앞에있는 요소를 뒤에 넣어줍니다.
                    move--;
                }
            }
            else if(move<0){
                deq.poll(); // 음수인 경우에는 양수와 반대로 poll을 해도 뒤에있는 요소를 앞으로 한번 넣어줘어야 move1번과 동일하기때문에 따로 move값에 변동을 주지 않았습니다.
                move = move%deq.size(); //음수인 경우에는 나머지가 음수이지만 실제 move 횟수와 동일한 음수중 가장 0에 가까운 값이 나옵니다. 자세한 것은 https://lasdri.tistory.com/812 를 참고해주세요.
                while (move < 0) {
                    deq.offerFirst(deq.pollLast()); //뒤에있는 요소를 앞에 넣어줍니다.
                    move++;
                }
            }
        }
        System.out.print(sb);
    }




    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() throws IOException{
            //br = new BufferedReader(new InputStreamReader(System.in)); //백준 제출 시 주석해제를 하면 됩니다.
            br = new BufferedReader(new FileReader("input.txt")); //IDE 실행 시 주석해제를 하면 됩니다.
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
