// Authored by : lms0806
// Co-authored by : -
// Link : http://boj.kr/ef8d43d74040402da1919de2e2607e4a
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException{
		FastReader rd = new FastReader();
		
		int size = rd.nextInt();
		
		StringBuilder sb = new StringBuilder();
		while(size --> 0) {
			int[] alpha = new int[26];
			
			for(char ch : rd.nextLine().toCharArray()) {
				if(ch != ' ') {
					alpha[ch - 'a']++;
				}
			}
			
			int max = 0, count = 0, n = 0;
			for(int i = 0; i < alpha.length; i++) {
				if(max < alpha[i]) {
					max = alpha[i];
					n = i;
					count = 0;
				}
				else if(max == alpha[i]) {
					count++;
				}
			}
			
			sb.append(count != 0 ? "?" : (char)(n + 'a')).append("\n");
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