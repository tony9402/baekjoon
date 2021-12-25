//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/4e4fa5497b7d4fad88ea6b0c69a1852d

import java.util.*;
import java.io.*;

public class Main {
    static boolean prime_num[]; // false면 소수 (단, 2 이상인 정수)
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        
        int a = rd.nextInt();
        int b = rd.nextInt();
        
        prime_num = new boolean[b + 1];
        
        check_prime(b);
        palindrome(a, b);
    }

    // 소수 판별 에라토스테네스의 체
    // 소수인 수의 배수들을 지우는 방식
    // 배수를 지울 때 끝 수(b)의 제곱근 이하 수 까지만 확인한다
    static void check_prime(int b) {
        for(int i = 2;i <= Math.sqrt(b);i++) {
            if(prime_num[i] == true) continue;
            for(int j = 2;i * j <= b;j++) 
                prime_num[i * j] = true;
        }
    }

    // 팰린드롬 판별
    static void palindrome(int a, int b) {
        for(int i = a;i <= b;i++) {
            if(prime_num[i] == false) { // 소수에 대해서만 확인
                // 펠린드롬 판별하고 하는 수를 문자열로 변환
                String str = Integer.toString(i);
                // 문자열로 변환한 수의 양 끝부터 중앙으로 같은지 검사
                int begin = 0;
                int end = str.length() - 1;
                boolean flag = true;   
                for(;begin < end;begin++, end--) {
                    if(str.charAt(begin) != str.charAt(end)) {
                        flag = false;
                        break;
                    }
                }
                if(flag == true) System.out.println(i);
            }
        }
        System.out.println("-1");
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
