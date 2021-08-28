// Authored by : lms0806
// Co-authored by : -
// Link : http://boj.kr/be72a03cff2a4722bdb5db5e31c0efdb
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[] num;
    public static void main(String[] args) throws IOException{
        FastReader rd = new FastReader();
        
        int size = rd.nextInt(), number = rd.nextInt();
        
        num = new int[size];
        
        for(int i = 0; i < size; i++) {
            num[i] = rd.nextInt();
        }
        
        System.out.print(solve(num, number));
    }
    
    public static int solve(int[] num, int number) {
        int answer = 0;
        
        for(int i = 0; i < num.length - 2; i++) {
            for(int j = i + 1; j < num.length - 1; j++) {
                for(int k = j + 1; k < num.length; k++) {
                    int temp = num[i] + num[j] + num[k];
                    
                    if(temp == number) {
                        return temp;
                    }
                    if(answer < temp && temp < number) {
                        answer = temp;
                    }
                }
            }
        }
        return answer;
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