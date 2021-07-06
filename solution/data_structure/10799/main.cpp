// Authored by : tallua_y
// Co-authored by : -
// Link : http://boj.kr/53875935b49b422486b56441978f7ad7
#include <iostream>

using namespace std;
using ull = unsigned long long;

int main(int argc, char** argv)
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ull total = 0;
    ull pipe_stack = 0;
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