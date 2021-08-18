// Authored by : lms0806
// Co-authored by : -
// Link : http://boj.kr/a2d39728db0c40a784b657882ee17fc7
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.TreeMap;

public class Main {
	public static void main(String[] args) throws IOException{
		FastReader rd = new FastReader();
		
		int size = rd.nextInt();
		
		TreeMap<String, Integer> map = new TreeMap<>();
		
		while(size --> 0) {
			String str = rd.nextLine();
			str = str.substring(str.indexOf(".") + 1);
			
			map.put(str, map.get(str) == null ? 1 : map.get(str) + 1);
		}
		
		StringBuilder sb = new StringBuilder();
		for(String key : map.keySet()) { 
			sb.append(key).append(" ").append(map.get(key)).append("\n"); 
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