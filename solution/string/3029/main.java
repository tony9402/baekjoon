import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 

		System.out.print(solve(br.readLine(), br.readLine()));
	}
	
	public static String solve(String s1, String s2) {
		
		if(s1.equals(s2)) {
			return "24:00:00";
		}
		
		int h = Integer.parseInt(s2.split(":")[0]) - Integer.parseInt(s1.split(":")[0]);
		int m = Integer.parseInt(s2.split(":")[1]) - Integer.parseInt(s1.split(":")[1]);
		int s = Integer.parseInt(s2.split(":")[2]) - Integer.parseInt(s1.split(":")[2]);
		
		if(s < 0) {
			s += 60;
			m--;
		}
		
		if(m < 0) {
			m += 60;
			h--;
		}
		
		if(h < 0) {
			h += 24;
		}
		
		return String.format("%02d:%02d:%02d", h, m, s);
	}
}