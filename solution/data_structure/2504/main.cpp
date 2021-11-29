// Authored by : tallua_y
// Co-authored by :
// Link : http://boj.kr/48252863d9ae4860b54cfceb442110ba
#include <bits/stdc++.h>

using namespace std;

struct Token {
    int value;
    size_t pos;
};

int main(int argc, char** argv)
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string input;
    cin >> input;

    vector<Token> tokens;
    tokens.push_back({ 0, '$' });
    for (size_t head = 0; head < input.size(); ++head) {
        if (input[head] == '(' || input[head] == '[') {
            tokens.push_back({ 0, head });
        } else {
            const auto open_tag = (input[head] == ')' ? '(' : '[');
            if (tokens.empty() || input[tokens.back().pos] != open_tag) {
                tokens.clear();
                break;
            }

            Token token = tokens.back();
            tokens.pop_back();

            const auto designated_value = (input[head] == ')' ? 2 : 3);
            if (token.pos + 1 == head) {
                tokens.back().value += designated_value;
            } else {
                tokens.back().value += token.value * designated_value;
            }
        }
    }

    if (tokens.size() != 1) {
        cout << "0\n";
    } else {
        cout << tokens.back().value << '\n';
    }

    return 0;
}