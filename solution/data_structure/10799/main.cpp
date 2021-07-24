// Authored by : tallua_y
// Co-authored by : -
// Link : http://boj.kr/6f2667a520d749d9adcee6ec0591da98
#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int total = 0;
    int pipe_stack = 0;
    bool is_opened = true;

    char ch;
    while (cin >> ch) {
        if (ch == '(') {
            // start of pipe
            pipe_stack++;
            is_opened = true;
        } else if (ch == ')' && is_opened) {
            // laser
            pipe_stack--;
            total += pipe_stack;
            is_opened = false;
        } else if (ch == ')' && !is_opened) {
            // end of pipe
            pipe_stack--;
            total += 1;
            is_opened = false;
        }
    }

    cout << total << '\n';

    return 0;
}
