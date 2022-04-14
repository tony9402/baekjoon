// Authored by : KimJeongSoo723
// Co-authored by : -
// Link : https://www.acmicpc.net/problem/10866


import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        FastReader rd = new FastReader();
        String input = rd.next();
        Stack<String> st = new Stack<>();

        int pipe = 0; // 레이저를 쏠 때 레이저가 관통하는 막대기가 몇개인지 체크하기 위한 변수입니다.
        int answer = 0; // pipe가 총 3개가 있고 그 3개를 레이저가 2번 관통한다고 하면 answer = pipe의 갯수+ pipe의 갯수*레이저가 관통한횟수 = 3 + 3*2 = 9임을 착안하여 풀이를 시작합니다.

        for(int i=0;i<input.length();i++){
            String now = input.substring(i,i+1);

            if(now.equals("(")) { // now == "(" 으로 작성시 false를 반환합니다. https://javanitto.tistory.com/9 를 참고해주세요.
                String next = input.substring(i+1,i+2);
                st.push("(");
                if(next.equals("(")){
                    pipe++; // 다음 문자열이 (인경우 레이저를 쏘지않고 기존에 있던 pipe에 한층 더 쌓습니다.
                    answer++; // pipe의 갯수를 체크하는 과정입니다.
                }
            }

            else{
                String before = input.substring(i-1,i);
                if(before.equals("(")) {
                    st.pop();
                    answer += pipe; //이전문자열이 (인경우 ()가 완성되므로 레이저를 쏘고 현재의 pipe 갯수만큼 answer에 추가해줍니다.
                }
                else{
                    st.pop();
                    pipe--; //이전문자열이 )인경우 레이저를 쏘는게 아니라 가장 상위에 있는 막대기를 제거합니다.
                }
            }
        }
        System.out.print(answer);
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
