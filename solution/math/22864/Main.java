package baekjoon_22864;

//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/9e22093a088c4facb197d261767247ba

import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) {
		FastReader rd = new FastReader();
		
		int A = rd.nextInt();
		int B = rd.nextInt();
		int C = rd.nextInt();
		int M = rd.nextInt();
		
		int time = 0;
		int tired = 0; //�Ƿε�
		int work = 0;
		while(time < 24) { //24�ð� ���� ��
			if(can_work(A, tired, M)) { // ���� �� �� ���� ��
				work += B;
				tired += A;
			}
			else {// ���� �� �� ���� �� => ����.
				tired -= C;
				if(tired < 0) tired = 0; //�Ƿε��� 0���� �۾����� �ʰ�
			}
			time++;
		}
		System.out.print(work);
	}
	static boolean can_work(int A, int tired, int M) {
		if(tired + A <= M) return true;
		else return false;
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