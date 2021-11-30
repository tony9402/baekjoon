//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/f6232bedc14545ecb59f0398d4826f7d

import java.util.*;
import java.io.*;

public class Main {
    static int[] num = new int[200010];
    static int[] count = new int[200010];
	
    public static void main(String[] args) {
        FastReader rd = new FastReader();

        int N = rd.nextInt();
        int K = rd.nextInt();
		
        for(int i = 1;i <= N;i++)
            num[i] = rd.nextInt();
		
        //투포인터로 풀이
        //start와 end사이에 겹치는 수가 K개 이하일 때는 end증가
        //K개 초과일 때는 start를 늘려가며 겹치는 수가 빠질때까지 begin증가
        int begin = 1, end = 1, max = 0;
        while(end <= N) {
            if(count[num[end]] < K) {
                max = Math.max(end - begin + 1, max);
                count[num[end]]++;
                end++;
            }
            else {
                max = Math.max(end - begin, max);
                //(end - 1) - begin + 1
                //end번째에 K를 초과하기 때문에 end - 1번째 까지
                //길이를 고려해야 함.
                count[num[begin]]--;
                begin++;
            }
        }
		
        System.out.println(max);
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
