// Authored by : lms0806
// Co-authored by : -
// Link : http://boj.kr/6d7b80bed5be4ae5b0b4cd97ebb73990
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[] num = {3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1};
	public static void main(String[] args) throws IOException{
		FastReader rd = new FastReader();
		
		int n = 0;
		for(char ch : rd.nextLine().toCharArray()) {
			n += num[ch - 'A'];
			if(n > 9) {
				n %= 10;
			}
		}
		System.out.print(n % 2 == 1 ? "I'm a winner!" : "You're the winner?");
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