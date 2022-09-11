// Authored by : J-TKim
// Co-authored by : -
// Link : http://boj.kr/b6fbe87e3cec4de0af83034de22af2cc
import java.lang.*;
import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        
        int N = rd.nextInt();

        StringBuilder out = new StringBuilder();

        for (int i=0; i < N; i++) {
            String str = rd.nextLine();
            char[] Line = str.toCharArray();
            
            int n = 0;
            int j = 0;
            for (; j < str.length(); j++) {
                char charNow = Line[j];
                
                if (charNow == '(') { n+=1; }
                else if (charNow == ')') {
                    if (n <= 0) { break; }
                    else { n-=1; }
                }
            }
            if (j == str.length() && n == 0) { out.append("YES\n"); }
            else { out.append("NO\n"); }
        }
        
        System.out.println(out);
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

        int nextInt() {
            return Integer.parseInt(next());
        }
        long nextLong() {
            return Long.parseLong(next());
        }
        double nextDouble() {
            return Double.parseDouble(next());
        }
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
