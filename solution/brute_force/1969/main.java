// Authored by : lms0806
// Co-authored by : -
// Link : http://boj.kr/9aa17da15fad46fb9ecb730bfdfda7f4
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        FastReader rd = new FastReader();

        int size = rd.nextInt(), size1 = rd.nextInt();
        
        String[] str = new String[size];
        
        for(int i = 0; i < size; i++) {
            str[i] = rd.nextLine();
        }
        
        int[][] num = new int[size1][26];
        
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < size1; i++) {
            for(int j = 0; j < size; j++) {
                num[i][str[j].charAt(i) - 'A']++;
            }
        }
        
        int count = 0;
        for(int i = 0; i < size1; i++) {
            int max = 0, n = 0;
            for(int j = 0; j < 26; j++) {
                if(max < num[i][j]){
                    max = num[i][j];
                    n = j;
                }
            }
            count += size - max;
            sb.append((char)(n + 'A'));
        }
        System.out.print(sb + "\n" + count);
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
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
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}