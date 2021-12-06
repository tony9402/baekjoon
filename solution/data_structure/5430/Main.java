//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/fc75d4683aa44fd5be618ed3934ac634

/*
시간이 빡빡해서 실제로 뒤집기, 삭제하기를 구현하면 안됩니다.
뒤집기는 실제로 뒤집는 것이 아닌 앞에서 뒤로 읽는걸 뒤에서 앞으로 읽게 하였고
삭제하기는 실제 삭제가 아닌 front포인터를 하나 증가시키는 식으로 구현했습니다.
출력도 빠른 출력을 해야 시간초과가 나지 않습니다. 
*/

import java.util.*;
import java.io.*;

public class Main {
    static ArrayList <String> numlist = new ArrayList<String>();
    static boolean reverse = false;
    static int front, end;
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        FastReader rd = new FastReader();

        int T = rd.nextInt();

        for(int i = 0;i < T;i++) {
            String p = rd.nextLine();
            int n = rd.nextInt();

            // inputString => tokenizer로 구분자 제거 후 list에 삽입
            InputString(rd.nextLine());

            boolean error = false;
            for(int j = 0;j < p.length();j++) {
                if(p.charAt(j) == 'R')  
                    ReverseList(); // ListReverse => 뒤집기

                else {
                    if(front > end) {
                        // 에러상황
                        // front가 end보다 큰 상황은 
                        // front == end == 1 인 상황(list에 값이 하나)에서
                        // 하나를 지운 후 상황이다. 즉 지울 것이 없는 상태
                        bw.write("error\n");
                        bw.flush();
                        error = true;
                        break;
                    }
                    else // 지울 수 있는 문자가 있을 때
                        DeleteList(); // DeleteList => 0번 인덱스 삭제
                }
            }
            if(error == false) OutputList();

            numlist.clear();
            reverse = false;
        }
        bw.close();
    }

    static void OutputList() throws IOException{
        bw.write("[");
        // reverse가 false면 정상상태 => 앞(front) 뒤(end)방향으로 출력
        if(reverse == false) {
            for(int i = front;i <= end;i++) {
                if(i == end) bw.write(numlist.get(i));
                else bw.write(numlist.get(i) + ","); 
            }
        }
        // reverse가 true면 뒤집힌 상태 => 뒤(end) 앞(front)방향으로 출력
        else {
            for(int i = end;i >= front;i--) 
                if(i == front) bw.write(numlist.get(i));
                else bw.write(numlist.get(i) + ",");
        }
        bw.write("]\n");
        bw.flush();
    }

    static void DeleteList() {
        // 실제로 지우는 것이 아닌 가리키는 인덱스를 증가 또는 감소시킴
        // 정상 상태이면 앞 인덱스를 증가(앞을 삭제하게 되므로)
        // 뒤집힌 상태이면 뒤 인덱스를 감소(뒤가 가장 앞이 되므로) 
        if(reverse == false) front++;
        else end--;
    }

    static void ReverseList() {
        // 실제로 뒤집는 것이 아닌 뒤집혀있는지 아닌지만 판단
        // 후에 출력할때 출력 순서를 바꾼다
        if(reverse == true) reverse = false;
        else reverse = true;
    }

    static void InputString(String numstr) {
        StringTokenizer st = new StringTokenizer(numstr, "[ | , | ]");

        while(st.hasMoreTokens()) 
            numlist.add(st.nextToken());

        front = 0;
        end = numlist.size() - 1;
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
