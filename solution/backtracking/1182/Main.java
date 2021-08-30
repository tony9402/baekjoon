// Authored by : lms0806
// Co-authored by : -
// Link : http://boj.kr/4ec78fe2e6674292a7179dc07a7718b3
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n, s;
    static int[] arr = new int[22];

    public static void main(String[] args) throws IOException {
        FastReader rd = new FastReader();

        n = rd.nextInt();
        s = rd.nextInt();

        for (int i = 0; i < n; i++) {
            arr[i] = rd.nextInt();
        }

        System.out.print(solve(false, 0, 0));
    }

    public static int solve(boolean flag, int idx, int num) {
        if (idx == n) { // 끝부분까지 갔을 때
            if (num == s && flag) { // flag가 true면 다 확인했고, 값이 같으므로 1
                return 1;
            }
            return 0; // 끝까지 갔으나 다르므로 0
        }

        return solve(true, idx + 1, num + arr[idx]) + solve(flag, idx + 1, num);
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}
