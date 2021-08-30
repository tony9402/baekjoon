// Authored by : lms0806
// Co-authored by : -
// Link : http://boj.kr/7105d879677a4ebb96ade9837f789f03
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int[] arr;
    public static void main(String[] args) throws IOException{
        FastReader rd = new FastReader();

        int size = rd.nextInt();

        arr = new int[size];

        for(int i = 0; i < size; i++) {
            arr[i] = rd.nextInt();
        }

        Arrays.sort(arr);

        size = rd.nextInt();

        StringBuilder sb = new StringBuilder();
        while(size --> 0) {
            sb.append(binary_search(0, arr.length - 1, rd.nextInt())).append(" ");
        }
        System.out.print(sb);
    }

    public static int binary_search(int start, int end, int n) {
        while(start <= end) {
            int mid = (start + end) / 2;
            if(arr[mid] == n) {
                return 1;
            }

            if(n < arr[mid]) end = mid - 1;
            else start = mid + 1;
        }
        return 0;
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
