// Authored by : lms0806
// Co-authored by : -
// Link : http://boj.kr/200735713a4a43b9a67e046187e1c2d9
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
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
		
		Arrays.sort(arr);
		
		int start = 1, end = arr[size - 1], answer = -1;
		while(start <= end) {
			int mid = (start + end) / 2;
			int count = 1, last = arr[0];
			
			for(int i = 1; i < size; i++) {
				if(arr[i] - last >= mid) {
					count++;
					last = arr[i];//차이 좁혀가기
				}
			}
			
			if(count >= num) {
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