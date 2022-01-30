//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/787dcc6cfe4648dc92d919982ad45f9e

import java.util.*;
import java.io.*;

public class Main {
    static ArrayList<String> IPv6 = new ArrayList<String>();
    public static void main(String[] args) {
        FastReader rd = new FastReader();

        String address = rd.nextLine();
        StringTokenizer st = new StringTokenizer(address, ":", true);

        // StringTokenizer로 ":"를 구분자로 나눈다
        // 나눈 토큰들을 IPv6리스트에 삽입
        while(st.hasMoreTokens()) 
            IPv6.add(st.nextToken());

        // IPv6리스트에서 1번규칙을 복원한다
        // 앞자리 생략된 "0" 복원
        int cnt = 0;
        for(int i = 0;i < IPv6.size();i++) {
            if(IPv6.get(i).equals(":")) continue;
            cnt++;
            for(int j = IPv6.get(i).length();j < 4;j++) 
                IPv6.set(i, "0" + IPv6.get(i));
        }

        // 위에서 복원된 리스트를 하나의 string으로 합침
        String ans = "";
        for(int i = 0;i < IPv6.size();i++) 
            ans += IPv6.get(i);

        // ans에 "::"가 존재하는 경우 (2번 규칙이 적용된 경우)
        // 위에서 부족한 횟수만큼 "0000:"으로 채우고
        // "::"와 대체한다
        if(ans.contains("::")) {
            String replace = ":";
            for(int i = cnt;i < 8;i++) 
                replace += "0000:";
            ans = ans.replace("::", replace);
        }

        // 주소의 맨 앞과 뒤에 ":"이 존재하는 경우 없애준다
        if(ans.charAt(ans.length() - 1) == ':') 
            ans = ans.substring(0, ans.length() - 1);
        if(ans.charAt(0) == ':') 
            ans = ans.substring(1, ans.length());

        System.out.println(ans);
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
