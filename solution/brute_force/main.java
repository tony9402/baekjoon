// Authored by : lms0806
// Co-authored by : -
// Link : http://boj.kr/96e89d739ab04f75ba9ee568aca10642
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        FastReader rd = new FastReader();
        
        int a = rd.nextInt(), b = rd.nextInt(), c = rd.nextInt();
        int m = rd.nextInt();
        
        int count = 0, p = 0, answer = 0;
        while(count != 24) {
            if(p + a <= m) {
                answer += b;
                p += a;
            }
            else {
                p = p - c < 0 ? 0 : p - c;
            }
            count++;
        }
        System.out.print(answer);
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