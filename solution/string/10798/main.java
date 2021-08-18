// Authored by : lms0806
// Co-authored by : -
// Link : http://boj.kr/3c8eb525866b4ac08270094c21906461
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static String[] str = new String[5];
	public static void main(String[] args) throws IOException{
		FastReader rd = new FastReader();
		
		for(int i = 0; i < 5; i++) {
			str[i] = rd.nextLine();
		}
		
		StringBuilder sb  = new StringBuilder();
		for(int i = 0; i < 15; i++) {
			for(int j = 0; j < 5; j++) {
				if(str[j].length() > i) {
					sb.append(str[j].charAt(i));
				}
			}
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