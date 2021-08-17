// Authored by : lms0806
// Co-authored by : -
// Link : http://boj.kr/806d668045d94b7197663986f1086ae3
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException{
		FastReader rd = new FastReader();
		
		String str = "";
		StringBuilder sb = new StringBuilder();
		while((str = rd.nextLine()) != null) {
			StringTokenizer st = new StringTokenizer(str);
			
			String s = st.nextToken(),t = st.nextToken();
			
			int count = 0;
			for(int i = 0; i < t.length(); i++) {
				if(t.charAt(i) == s.charAt(count)) {
					count++;
				}
				if(count == s.length()) {
					break;
				}
			}
			sb.append(count == s.length() ? "Yes" : "No").append("\n");
		}
		System.out.print(sb);
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