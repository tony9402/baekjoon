// Authored by : lms0806
// Co-authored by : -
// Link : http://boj.kr/9dc3aac345e548aea4453fef28ff9c26
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException{
		FastReader rd = new FastReader();
		
		StringBuilder sb = new StringBuilder(), ss = new StringBuilder();
		
		boolean istrue = false;
		for(char ch : rd.nextLine().toCharArray()) {
			if(ch == '<' || ch == ' ') {
				sb.append(ss.reverse());
				ss.setLength(0);
				sb.append(ch);
				if(ch == '<') {
					istrue = true;
				}
			}
			else if(ch == '>') {
				istrue = false;
				sb.append(ch);
			}
			else {
				if(istrue) {
					sb.append(ch);
				}
				else {
					ss.append(ch);
				}
			}
		}
		if(ss.length() != 0) {
			sb.append(ss.reverse());
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