// Authored by : lms0806
// Co-authored by : -
// Link : http://boj.kr/91161b29442545bd8335d4e292d0d507
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        FastReader rd = new FastReader();
        System.out.print(solve(rd.nextLine(), rd.nextLine()));
    }

    public static String solve(String s1, String s2) {
        if(s1.equals(s2)) {
            return "24:00:00";
        }

        int h = Integer.parseInt(s2.split(":")[0]) - Integer.parseInt(s1.split(":")[0]);
        int m = Integer.parseInt(s2.split(":")[1]) - Integer.parseInt(s1.split(":")[1]);
        int s = Integer.parseInt(s2.split(":")[2]) - Integer.parseInt(s1.split(":")[2]);

        if(s < 0) {
            s += 60;
            m--;
        }

        if(m < 0) {
            m += 60;
            h--;
        }

        if(h < 0) {
            h += 24;
        }

        return String.format("%02d:%02d:%02d", h, m, s);
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
