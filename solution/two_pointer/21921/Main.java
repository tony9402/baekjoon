package baekjoon_21921;

//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/1c1a979d8e70465fbe6b2aed1835549a

import java.util.*;
import java.io.*;

public class Main {
	static int[] day = new int[250010];
	static int[] sum = new int[250010];
	
	public static void main(String[] args) {
		FastReader rd = new FastReader();

		int N = rd.nextInt();
		int X = rd.nextInt();
		//i��°���� ���� �湮�� �� ���ϱ�
		for(int i = 1;i <= N;i++) {
			day[i] = rd.nextInt();
			sum[i] = sum[i - 1] + day[i];
		}
		
		int max = 0; //�ִ�� �湮�� ���� �湮�� ��
		int cnt = 0; //�ִ�� �湮�� ���� ��
		for(int i = X;i <= N;i++) {
			//�����̵� ������ ������� X�ϸ�ŭ �湮�� ���� ���ؼ�
			int tmp = sum[i] - sum[i - X];
			//max������ ũ�� max�� ���� ��
			//�Ⱓ�� 1�� �ʱ�ȭ
			if(tmp > max) {
				max = tmp;
				cnt = 1;
			}
			//max���� ������ ���� �� �ִ°�� �Ⱓ����
			else if(tmp == max) cnt++;
		}
		
		if(max == 0) System.out.println("SAD");
		else System.out.println(max + "\n" + cnt);
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