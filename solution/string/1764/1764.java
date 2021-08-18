// Authored by : lms0806
// Co-authored by : -
// Link : http://boj.kr/7f6347f348fd48a7a0e88ff7aef7e6b7
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException{
		FastReader rd = new FastReader();
		
		int n = rd.nextInt(), m = rd.nextInt();
		
		HashSet<String> strs = new HashSet<>();
		ArrayList<String> strss = new ArrayList<>();
		
		while(n --> 0) {
			strs.add(rd.nextLine());
		}
		
		int answer = 0;
		String str = "";
		while(m --> 0) {
			str = rd.nextLine();
			if(strs.contains(str)) {
				strss.add(str);
				answer++;
			}
		}
		
		Collections.sort(strss);
		
		StringBuilder sb = new StringBuilder();
		sb.append(answer).append("\n");
		for(String s : strss) {
			sb.append(s).append("\n");
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