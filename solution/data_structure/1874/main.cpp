// Authored by : tallua_y
// Co-authored by :
// Link : http://boj.kr/98f5daa8e3a3430cb4a5998327fd56cf
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char** argv)
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    int remain = 1;
    vector<int> stack;
    stack.reserve(N);

    vector<char> answer;
    answer.reserve(2 * N + 1);

    for (int n = 0; n < N; ++n) {
        int current;
        cin >> current;

        while (remain <= current) {
            stack.push_back(remain++);
            answer.push_back('+');
            answer.push_back('\n');
        }

        if (!stack.empty() && stack.back() == current) {
            stack.pop_back();
            answer.push_back('-');
            answer.push_back('\n');
        } else {
            answer.clear();
            answer.push_back('N');
            answer.push_back('O');
            answer.push_back('\n');
            break;
        }
    }

    // make c string
    answer.push_back(0);
    cout << answer.data();

    return 0;
}