// Authored by : lms0806
// Co-authored by : -
// Link : http://boj.kr/72e516ae033949fba8f5ab0b042e4364
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[] arr;
	public static void main(String[] args) throws IOException{
		FastReader rd = new FastReader();
		
		int size = rd.nextInt(), num = rd.nextInt();
		
		arr = new int[size];
		
		for(int i = 0; i < size; i++) {
			arr[i] = rd.nextInt();
		}
		
		long end = arr[0];
		for(int n : arr) {
			end = Math.max(end, n);
		}
		
		long start = 0, answer = -1;
		while(start <= end) {
			long mid = (start + end) / 2, now = 0;
			
			for(int n : arr) {
				now += Math.max(0, n - mid);
				if(now >= num) {
					break;
				}
			}
			
			if(now >= num) {
				answer = mid;
				start = mid + 1;//start 차이 좁혀가기
			}
			else {
				end = mid - 1;//end 차이 좁혀가기
			}
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