//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/44f8ca6f58d443b492bc1641ffc6e2a1

import java.util.*;
import java.io.*;

class Pair implements Comparable<Pair> {
    int loc, cnt;
    Pair(int loc, int cnt){
        this.loc = loc;
        this.cnt = cnt;
    }
    @Override
    public int compareTo(Pair p) {
        return this.loc - p.loc;
    }
}

public class Main {
    static ArrayList<Pair> village;
    public static void main(String[] args) {
        FastReader rd = new FastReader();

        int N = rd.nextInt();
        village = new ArrayList<Pair>(N + 10);

        // 위치와 인구수를 입력받으면서 전체 인구수를 구합니다.
        long sum_cnt = 0;
        for(int i = 0;i < N;i++) {
            int loc = rd.nextInt();
            int cnt = rd.nextInt();
            village.add(new Pair(loc, cnt));
            sum_cnt += cnt;
        }

        // (전체 인구수 + 1) / 2가 중심이고 우체국이 설치되어야 하는 위치
        // +1을 하는 이유는 인원수가 많은 쪽에 우체국을 설치해야 하기 때문
        // 마을 순서대로 정렬합니다 -> 오름차순
        Collections.sort(village);
        long half = (sum_cnt + 1) / 2; 

        // 1번 마을부터  인구수를 더해가며 중간 값 이상이 되면 그곳에 우체국을 설치합니다
        long sum = 0;
        for(int i = 0;i < village.size();i++) {
            sum += village.get(i).cnt;
            if(sum >= half) {
                System.out.println(village.get(i).loc);
                break;
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
