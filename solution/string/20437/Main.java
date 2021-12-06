//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/0d345a8508a74a1fbf363c6719797709

/* 
3. 어떤문자를 정확히 k개 포함하는 가장 짧은 문자열
== 시작과 끝이 어떤 문자인 가장 짧은 문자열
4. 어떤문자가 시작과 끝이고 정확히 k개 포함하는 가장 긴 문자열
== 시작과 끝이 어떤 문자인 가장 긴 문자열  
*/

import java.util.*;
import java.io.*;

public class Main {
    static int[] alpha = new int[26];

    public static void main(String[] args) {
        FastReader rd = new FastReader();

        int T = rd.nextInt();

        for(int i = 0;i < T;i++) {

            // 초기화 
            for(int j = 0;j < 26;j++) 
                alpha[j] = 0;

            String W = rd.nextLine();
            int K = rd.nextInt();

            // 각 알파벳이 몇번 나왔는지 센다
            for(int j = 0;j < W.length();j++) 
                alpha[W.charAt(j) - 'a']++;

            int min = Integer.MAX_VALUE, max = 0;
            for(int j = 0;j < W.length();j++) {
                if(alpha[W.charAt(j) - 'a'] < K) continue;

                // K보다 크거나 같은 빈도로 나온 문자만 본다
                // 그 문자가 문자열의 시작과 끝
                char ch = W.charAt(j);
                int count = 0;
                for(int l = j;l < W.length();l++) {
                    if(ch != W.charAt(l)) continue;
                    else count++;

                    // 정확히 K개가 되는 순간 min, max값 갱신
                    if(count == K) {
                        min = Math.min(min, l - j + 1);
                        max = Math.max(max, l - j + 1);
                        break;
                    }
                }
            }

            if(min == 10001 || max == 0) System.out.println("-1");
            else System.out.println(min + " " + max);
        }
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
