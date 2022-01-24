//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/28ba7ff8e9884d89a27e620ed389d657

import java.util.*;
import java.io.*;

public class Main {
    static int paper[][];
    static int zero, one, m_one;
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        
        int N = rd.nextInt();
        paper = new int[N][N];
        for(int i = 0;i < N;i++) {
            for(int j = 0;j < N;j++)
                paper[i][j] = rd.nextInt();
        }
        
        recur(0, 0, N);
        System.out.println(m_one + "\n" + zero + "\n" + one);
    }
    
    // sy와 sx는 시작위치, size는 검사할 영역의 크기입니다
    static void recur(int sy, int sx, int size) {
        // num은 기준숫자
        int num = paper[sy][sx];

        boolean isSame = true;
        for(int i = sy;i < sy + size;i++) {
            for(int j = sx;j < sx + size;j++) {
                // 다른 숫자가 존재하는 경우
                if(num != paper[i][j]) { 
                    isSame = false;
                    break;
                }
            }
        }
        
        // 종이의 숫자가 모두 같은 경우
        // 기준숫자 num값에 따라 결과값을 증가시킨다
        if(isSame) { 
            switch(num) {
            case -1:
                m_one++;
                break;
            case 0:
                zero++;
                break;
            default:
                one++;
                break;
            }
            return;
        }
        // 숫자들이 다른 경우 9등분 하여 다시 검사합니다
        else { 
            int sz = size / 3;
            for(int i = 0;i < 3;i++) {
                for(int j = 0;j < 3;j++) 
                    recur(sy + i * sz, sx + j * sz, sz);
            }
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
