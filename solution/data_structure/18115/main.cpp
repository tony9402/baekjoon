// https://www.acmicpc.net/problem/18115
// 2022-04-14 03:51:16 244ms
// by r4pidstart
#include<bits/stdc++.h>
using namespace std;

int main(void)
{
    int n; scanf("%d", &n);

    vector<int> cmd(n);
    for(int i=0; i<n; i++)
        scanf("%d", &cmd[i]);

    // 앞에서도, 뒤에서도 카드를 다루기에 덱이 적합하다
    deque<int> dq;

    // 마지막으로 내려놓은 카드부터, 차례대로 처리한다
    for(int i=n-1; i>=0; i--)
    {
        // i번째에 내려놓은 카드는 n-i번 카드이다.
        if(cmd[i] == 1)
            dq.push_front(n-i);
        else if(cmd[i] == 2)
            dq.insert(dq.begin()+1, n-i);
        else // if(cmd[1] == 3)
            dq.push_back(n-i);
    }

    // dq에 정리된 카드를 순서대로 출력한다
    for(auto i : dq)
        printf("%d ", i);
}

/*
    
*/
