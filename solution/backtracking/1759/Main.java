//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/9007cb16300c4b71aab8f755f4043b17

import java.util.*;
import java.io.*;

public class Main {
    static ArrayList<String> alpha;
    static String ans = "";
    static int L, C;
    public static void main(String[] args) {
        FastReader rd = new FastReader();

        L = rd.nextInt();
        C = rd.nextInt();
        
        alpha = new ArrayList<String>(C + 10);
        for(int i = 0;i < C;i++) 
            alpha.add(rd.next());
        
        // 오름차순으로 정렬한다
        Collections.sort(alpha);
        
        dfs(0, 0);
    }
    
    // dfs로 오름차순으로 만들어지는 모든 경우를 찾는다
    // 그중 모음 1개 이상, 자음 2개이상인 경우만 출력한다
    static void dfs(int idx, int size) {
        if(size == L) {
            int vowels = 0;
            int consonants = 0;
            for(int i = 0;i < L;i++) {
                switch(ans.charAt(i)) {
                case 'a': case 'e': case 'i': case 'o': case 'u':
                    vowels++;
                    break;
                default:
                    consonants++;
                    break;
                }
            }
            if(vowels >= 1 && consonants >= 2) 
                System.out.println(ans);
            return;
        }
        
        for(int i = idx;i < alpha.size();i++) {
            ans += alpha.get(i);
            dfs(i + 1, size + 1);
            ans = ans.substring(0, ans.length() - 1);
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
