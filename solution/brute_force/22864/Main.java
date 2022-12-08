//Authored by : marha-hwang
//Co-authored by : -
//Link : http://boj.kr/5e4f2a2c7d4d46c2941c7ebe75e4c74e
import java.util.*;
import java.io.*;
public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(in.readLine());
		
  //입력받기
		int A = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int answer = 0;
  
  //피로회복도가 최대피로도를 넘어가는 경우에 대한 예외 처리
		if(C > M) C = M;
		
  //x는 일을 수행한 시간, y는 휴식을 취한 시간
		for(int x = 1; x<=24; x++) {
			int y = 24 - x;
			if(A > M) break;
			if(A*x-C*y<=M && answer<B*x) answer = B*x;  
		}

		System.out.print(answer);
	}
}
