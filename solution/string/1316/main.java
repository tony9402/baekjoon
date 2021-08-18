// Authored by : lms0806
// Co-authored by : -
// Link : http://boj.kr/de995483538e4f32b2e3bacb12a79832
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static boolean[] alpha;
	public static void main(String[] args) throws IOException{
		FastReader rd = new FastReader();
		
		int size = rd.nextInt();
		
		int answer = 0;
		while(size --> 0) {
			String str = rd.nextLine();
			
			alpha = new boolean[26];
			
			alpha[str.charAt(0) - 'a'] = true;
			boolean istrue = true;
			for(int i = 1; i < str.length(); i++) {
				char ch = str.charAt(i);
				if(alpha[ch - 'a'] && ch != str.charAt(i - 1)) {
					istrue = false;
					break;
				}
				if(!alpha[ch - 'a']) {
					alpha[ch - 'a'] = true;
				}
			}
			answer += istrue ? 1 : 0;
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