import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt()+1;

        int[] O = new int[N];
        int[] A = new int[N];
        long[] S = new long[N];

        if(N > 1){
            for(int i=1; i<N; i++){
                O[i] = sc.nextInt();
                A[i] = A[i-1] + O[i];
            }

            //S[2] = O[1] * O[2];
            for(int i=2; i<N; i++){
                S[i] = S[i-1] + A[i-1]*O[i];
            }

            System.out.println(S[N-1]);
        }else{
            System.out.println(0);
        }

    }
}