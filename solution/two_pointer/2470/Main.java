//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/c3a386dd593e49dabc910fc56adfe5fd

import java.util.*;
import java.io.*;

public class Main {
    static ArrayList<Integer> sol;
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        
        int N = rd.nextInt();
        sol = new ArrayList<Integer>(N + 10);
        for(int i = 0;i < N;i++) 
            sol.add(rd.nextInt());
        
        // 입력받은 용액들을 오름차순으로 정렬합니다.
        Collections.sort(sol);
        
        // 양 끝부터 시작하여 가운데로 이동하며 최소값을 찾습니다.
        // 두 포인터의 합이 0보다 작거나 같으면 front를 증가시켜
        // 합이 0에 가까워지게 합니다 (반대 상황은 end를 감소시킵니다)
        // min값이 갱신될 때 두 포인터의 인덱스를 저장하여 최종 출력합니다
        int front = 0, ans_front = 0, ans_end = 0;
        int end = sol.size() - 1;
        int min = Integer.MAX_VALUE;
        while(front < end) {
            if(min > Math.abs(sol.get(front) + sol.get(end))) {
                min = Math.abs(sol.get(front) + sol.get(end));
                ans_front = front;
                ans_end = end;
            }
            if(sol.get(front) + sol.get(end) <= 0) 
                front++;
            else 
                end--;
        }
        System.out.println(sol.get(ans_front) + " " + sol.get(ans_end));
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
