import java.io.*;
import java.util.*;


class Ingredient {
    int b, s;

    Ingredient(int b, int s) {
        this.b = b;
        this.s = s;
    }
}




public class Main {

    static int n;
    static Ingredient[] a;

    static long calc(int bit) {
        long bitter = 0;
        long sour = 0;

        for (int k=0; k<n; k++) {
            if ((bit&(1<<k)) != 0) {
                bitter = bitter == 0 ? a[k].b : bitter*a[k].b;
                sour += a[k].s;
            }
        }

        return Math.abs(bitter-sour);

    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        a = new Ingredient[n];

        for (int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int b = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            a[i] = new Ingredient(b, s);
        }

        long ans = -1;
        for (int i=1; i<(1<<n); i++) {
            long tmp = calc(i);
            if (ans == -1 || ans != -1 && ans > tmp) ans = tmp;
        }

        System.out.println(ans);

    }
}