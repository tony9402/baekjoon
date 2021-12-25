//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/2e98c8f8a8b54b428eb5bc4a00e17491

import java.util.*;
import java.io.*;

class Problem implements Comparable<Problem> {
    int num, level;
    Problem(int num, int level){
        this.num = num;
        this.level = level;
    }
    // 난이도로 내림차순 정렬을 먼저 한 뒤
    // 같은 난이도에 대해서는 문제번호로 내림차순 정렬
    @Override
    public int compareTo(Problem op) {
        if(level < op.level) return 1;
        else if(level == op.level) {
            if(num < op.num) return 1;
            else if(num == op.num) return 0;
            else return -1;
        }
        else return -1;
    }
}

public class Main {
    static TreeSet<Problem> tset = new TreeSet<Problem>();
    static int[] problem = new int[100010];
    public static void main(String[] args) {
        FastReader rd = new FastReader();
        int N = rd.nextInt();
        
        // problem 배열에서 문제번호와 난이도를 저장하고
        // TreeSet을 이용하여 난이도, 문제번호 순으로 정렬합니다.
        for(int i = 0;i < N;i++) {
            int num = rd.nextInt();
            int lev = rd.nextInt();
            tset.add(new Problem(num, lev));
            problem[num] = lev;
        }

        int M = rd.nextInt();
        for(int i = 0;i < M;i++) {
            String command = rd.next();
            
            // "add" 명령시 TreeSet과 problem 배열에 추가
            if(command.equals("add")) {
                int num = rd.nextInt();
                int lev = rd.nextInt();
                tset.add(new Problem(num, lev));
                problem[num] = lev;
            }
            // "solved" 명령시 입력받은 문제번호와
            // 저장해놓은 문제번호의 난이도를 배열에서 찾은 후
            // TreeSet에서 삭제합니다.
            else if(command.equals("solved")) {
                int num = rd.nextInt();
                tset.remove(new Problem(num, problem[num]));
            }
            // recommend 1 은 가장 어렵고 큰 번호 이므로 첫 번째 값
            // recommend 2 는 가장 쉽고 작은 번호 이므로 마지막 값
            else {
                int n = rd.nextInt();
                if(n == 1) 
                    System.out.println(tset.first().num);
                else 
                    System.out.println(tset.last().num);
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
