//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/e64ec64074174f93bc1480b2da768894

import java.util.*;
import java.io.*;

public class Main {
    static ArrayList<Integer> crane, box;
    public static void main(String[] args) {
        FastReader rd = new FastReader();

        int N = rd.nextInt();
        crane = new ArrayList<Integer>(N + 10); 
        for(int i = 0;i < N;i++)
            crane.add(rd.nextInt());

        int M = rd.nextInt();
        box = new ArrayList<Integer>(M + 10);
        for(int i = 0;i < M;i++) 
            box.add(rd.nextInt());

        // 입력받은 상자와 크레인 정보를 내림차순으로 정렬합니다
        Collections.sort(crane, Collections.reverseOrder());
        Collections.sort(box, Collections.reverseOrder());

        // 옮길 수 없는 상황일 때 -1을 출력합니다.
        if(crane.get(0) < box.get(0)) {
            System.out.println("-1");
            return;
        }

        int time = 0, c_idx = 0, b_idx = 0;
        while(!box.isEmpty()) {
            // 옮길 수 있는 경우 그 상자를 제거합니다.
            if(box.get(b_idx) <= crane.get(c_idx)) {
                box.remove(b_idx);
                c_idx++;
                b_idx = 0;
            }
            // 옮길 수 없는 경우 다음 상자를 옮길 수 있는지 확인해 보기 위해
            // 다음 박스 인덱스값으로 이동
            else b_idx++;
            
            // 확인가능한 크레인이나 박스를 끝까지 살핀 경우
            // 1분 내 옮기기 가능한 모든 박스를 옮긴 상황
            // 따라서 1분이 추가됩니다.
            if(c_idx == N || b_idx == box.size()) {
                time++;
                c_idx = 0;
                b_idx = 0;
            }
        }
        System.out.println(time);
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
