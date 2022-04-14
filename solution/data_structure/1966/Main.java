// Authored by : KimJeongSoo723
// Co-authored by : -
// Link : https://www.acmicpc.net/problem/1966


import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        FastReader input = new FastReader();
        int n = input.nextInt();

        while(n--> 0) {
            Queue <int []> q  = new LinkedList<>();
            int doclength = input.nextInt();
            int wantedindex = input.nextInt();
            String[] priority = input.nextLine().split(" ");
            int count = 0;

            for (int i = 0; i < doclength; i++) {
                int now = Integer.parseInt(priority[i]);
                q.offer(new int[]{i, now});
            }//현재 q에 index와 우선순위를 집어넣습니다. index를 넣는 이유는 나중에 여기에 저장된 index가 문제에서 주어진 wantedindex와 같은경우를 확인하기 위함입니다.

            Arrays.sort(priority); // 우선순위를 정렬해서 (1~9의 범위를 가지는 string간의 비교이기때문에 sort만 해주어도 됩니다.만약 문제에서  우선순위가 두자리수이상으로 제시한다면 다른방법을 써야합니다.)
            int max = Integer.parseInt(priority[doclength-1]); // 정렬된 배열의 끝에있는 값이 최대값이 됩니다.

            while (q.size() > 0) {
                if (q.peek()[1] < max) {
                    int[] first = q.poll();
                    q.offer(first);
                } else {
                    count++;
                    if (q.peek()[0] == wantedindex) break; // 구하고자하는 조건에 만족하기 때문에 반복문을 종료하고 count를 출력합니다.
                    else {
                        q.poll();
                        max = Integer.parseInt(priority[doclength - 1 - count]); //제일 큰 값을 q에서 제외시키고 그 다음으로큰 max를 지정해줍니다.
                    }
                }
            }
            System.out.println(count);
        }
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
