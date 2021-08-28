// Authored by : lms0806
// Co-authored by : -
// Link : http://boj.kr/a148c3f38c3e452bacf72253f42ff47a
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        FastReader rd = new FastReader();

        System.out.print(solve(rd.nextInt()));
    }

    public static int solve(int n) {

        for (int i = 1; i < n; i++) {
            int number = i, num = 0;

            while (number != 0) {
                num += number % 10;
                number /= 10;
            }

            if (num + i == n) {
                return i;
            }
        }
        return 0;
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