//Authored by : suin8
//Co-authored by : -
//Link : 

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        FastReader rd = new FastReader();
		
        String input = rd.nextLine();
            
        //입력받은 문장을 +,-를 포함하여 토큰화
        StringTokenizer stk = new StringTokenizer(input, "+ | -", true);
            
        //첫 마이너스 이전은 모두 더하고 
        //이후에 모든 수를 빼면 최소값이 된다.
        boolean minus = false;
        int sum = 0;
        while(stk.hasMoreTokens()) {
            String token = stk.nextToken();
			
            if(token.equals("+")) continue;
            else if(token.equals("-")) minus = true;
            else {
                if(minus == true) sum -= Integer.parseInt(token);
                else sum += Integer.parseInt(token);
            }
        }
		
        System.out.print(sum);
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
