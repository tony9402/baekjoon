// Authored by : lms0806
// Co-authored by : -
// Link : http://boj.kr/357d1c53b8254bcd8f83b1209cc52daf
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        FastReader rd = new FastReader();

        int a = rd.nextInt(), b = rd.nextInt(), c = rd.nextInt();
        int d = rd.nextInt(), e = rd.nextInt(), f = rd.nextInt();
        
        System.out.print(solve(a,b,c,d,e,f));
    }

    public static String solve(int a, int b, int c, int d, int e, int f) {
        for(int x = -999; x <= 999; x++) {
            for(int y = -999; y <= 999; y++) {
                if(a * x + b * y == c && d * x + e * y == f) {
                    return x + " " + y;
                }
            }
        }
        return "";
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