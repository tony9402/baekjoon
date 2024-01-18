import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt()+1;

        int[] O = new int[N];
        int[] A = new int[N];

        for(int i=1; i<N; i++){
            O[i] = sc.nextInt();
            A[i] = A[i-1] + O[i];
        }

        long sum = 0;
        for(int i=1; i<N; i++){
            sum += A[i-1]*O[i];
        }

        System.out.println(sum);
    }
}