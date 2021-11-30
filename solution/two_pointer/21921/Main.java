//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/1c1a979d8e70465fbe6b2aed1835549a

import java.util.*;
import java.io.*;

public class Main {
    static int[] day = new int[250010];
    static int[] sum = new int[250010];
	
    public static void main(String[] args) {
        FastReader rd = new FastReader();

        int N = rd.nextInt();
        int X = rd.nextInt();
	    
        //i번째까지 누적 방문자 수 구하기
        for(int i = 1;i <= N;i++) {
            day[i] = rd.nextInt();
            sum[i] = sum[i - 1] + day[i];
        }
		
        int max = 0; //최대로 방문한 누적 방문자 수
        int cnt = 0; //최대로 방문한 날의 수
        for(int i = X;i <= N;i++) {
            //슬라이딩 윈도우 방식으로 X일만큼 방문자 수를 구해서
            int tmp = sum[i] - sum[i - X];
		
            //max값보다 크면 max값 갱신 후
            //기간을 1로 초기화
            if(tmp > max) {
                max = tmp;
                cnt = 1;
            }
		
            //max값과 동일한 날이 또 있는경우 기간증가
            else if(tmp == max) cnt++;
        }
		
        if(max == 0) System.out.println("SAD");
        else System.out.println(max + "\n" + cnt);
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
