import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] A = new int[N];
        int[] B = new int[M];

        st = new StringTokenizer(br.readLine(), " ");
        for(int i=0; i<N; i++){
            A[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine(), " ");
        for(int i = 0; i<M; i++){
            B[i] = Integer.parseInt(st.nextToken());
        }

        int x = 0;
        int y = 0;
        StringBuilder sb = new StringBuilder();
				// 정렬
        for(int i=0; i<M+N; i++){
            if(x == N) sb.append(B[y++]).append(" ");
            else if(y == M) sb.append(A[x++]).append(" ");
            else {
                if (A[x] > B[y]) sb.append(B[y++]).append(" ");
                else if (A[x] <= B[y]) sb.append(A[x++]).append(" ");
            }
        }
        sb.delete(sb.length()-1, sb.length());
        System.out.println(sb);

    }
}