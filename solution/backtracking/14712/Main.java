import java.io.*;
import java.util.*;
import java.lang.*;

public class Main {
    static int [][]map;
    static int N, M;
    static int answer;
    static public void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] line = br.readLine().split(" ");
        N = Integer.parseInt(line[0]);
        M = Integer.parseInt(line[1]);

        map = new int[N + 1][M + 1]; // 1-index
        
        dfs(0);

        System.out.println(answer);
    }

    static void dfs(int cnt) {
        if(cnt == N * M) {
            answer ++;
            return ;
        }
        int y = cnt / M + 1;
        int x = cnt % M + 1;
        
        if(map[y - 1][x] == 1 && map[y][x - 1] == 1 && map[y - 1][x - 1] == 1) { // 현재 놓을 수 없는 곳
            dfs(cnt + 1);
        }
        else {
            dfs(cnt + 1); // 선택 안하고 다음껄 볼 경우
            map[y][x] = 1;
            dfs(cnt + 1); // 선택 하고 다음껄 볼 경우
            map[y][x] = 0;
        }
    }
}
