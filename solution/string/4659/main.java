// Authored by : lms0806
// Co-authored by : -
// Link : http://boj.kr/1e73fdef646c45e784d1f5f3f083bb20
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException{
		FastReader rd = new FastReader();
		
		StringBuilder sb = new StringBuilder();
		while(true) {
			int counta = 0, countb = 0;
			boolean istrue = false;
			
			String str = rd.nextLine();
			
			if(str.equals("end")) {
				break;
			}
			char ch0 = str.charAt(0);
			
			if(ch0 == 'a' || ch0 == 'e' || ch0 == 'i' || ch0 == 'o' || ch0 == 'u') {
				counta++;
				istrue = true;
			}
			else {
				countb++;
			}
			
			for(int i = 1; i < str.length(); i++) {
				char ch = str.charAt(i);
				
				if(ch == str.charAt(i-1) && ch != 'e' && ch != 'o') {
					istrue = false;
					break;
				}
				if(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
					counta++;
					countb = 0;
					istrue = true;
				}
				else {
					countb++;
					counta = 0;
				}
				if(counta == 3 || countb == 3) {
					istrue = false;
					break;
				}
				
			}
			sb.append("<").append(str).append("> is ").append(istrue ? "" : "not ").append("acceptable.").append("\n");
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